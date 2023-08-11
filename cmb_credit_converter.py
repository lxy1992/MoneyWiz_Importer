import pandas as pd


def add_category_column(data):
    categories = {
        "还款": "Repayment",
        "分期": "Installment",
        "退款": "Refund",
        "消费": "Consumption"
    }
    current_category = None
    data['Category'] = None
    for index, row in data.iterrows():
        first_cell = str(row[0])
        if first_cell in categories:
            current_category = categories[first_cell]
        else:
            data.at[index, 'Category'] = current_category
    cleaned_data = data.dropna(subset=['Category'])
    return cleaned_data


def extract_currency(row):
    amount_str = str(row['交易地金额'])
    if '(' in amount_str and ')' in amount_str:
        return amount_str.split('(')[-1].split(')')[0]
    else:
        return 'CN'


def determine_income_expense(row):
    if row['Category'] in ['Repayment', 'Refund']:
        income = abs(float(row['交易地金额'].replace(',', '').strip()))
        expense = 0
    else:
        income = 0
        expense = abs(float(row['交易地金额'].replace(',', '').strip()))
    return income, expense


def replace_substrings(description):
    substrings_to_remove = ["支付宝-", "财付通-", "美团-"]
    for substring in substrings_to_remove:
        description = description.replace(substring, "")
    return description.strip()


def main(input_file, output_file):
    # Load CSV file
    data = pd.read_csv(input_file)

    # Add category column
    cleaned_data = add_category_column(data)

    # Add year to '交易日' and '记账日' columns
    cleaned_data['交易日'] = '2023/' + cleaned_data['交易日'].astype(str)
    cleaned_data['记账日'] = '2023/' + cleaned_data['记账日'].astype(str)

    # Extract currency and add to new column
    cleaned_data['货币'] = cleaned_data.apply(extract_currency, axis=1)
    cleaned_data['交易地金额'] = cleaned_data['交易地金额'].str.replace(r'\(.*\)', '', regex=True).str.strip()

    # Add new date column based on category
    cleaned_data['日期'] = cleaned_data.apply(
        lambda row: row['记账日'] if row['Category'] in ['Refund', 'Installment', 'Repayment'] else row['交易日'],
        axis=1)

    # Add income and expense columns
    cleaned_data['收入'], cleaned_data['支出'] = zip(*cleaned_data.apply(determine_income_expense, axis=1))

    # Replace specified substrings in '交易摘要' column
    cleaned_data['交易摘要'] = cleaned_data['交易摘要'].apply(replace_substrings)

    # Save the cleaned data to CSV
    cleaned_data.to_csv(output_file, index=False)
