# MoneyWiz Importer
- [中文文档](https://github.com/lxy1992/alipay_moneywiz_importer/blob/master/README_CN.md)

## Introduction
This is a script collection contains 
- Alipay Bill To MoneyWiz, converts Alipay bill to MoneyWiz CSV format.
- China Merchants Bank Credit Bill to MoneyWize, converts China Merchants Bank Credit bill to MoneyWiz CSV format.

## Alipay Bill To MoneyWiz
### Function
- remove the first 4 line about account info, only keep the bill transactions
- remove empty lines
- process alipay bad format in csv, such as misuse about comma and tab
- add 收 and 支 columns, which represent income and expense, it fits MoneyWiz's CSV format about income and expense

### How to Use
1. download the alipay bill csv file
2. install the Python 3.10 environment
3. activate the Python 3.10 virtualenv ```source venv/bin/activate```
4. run
```pip install -r requirements.txt```
5. Run script

```python
from alipay_converter import *

input_file = 'your_path/alipay_bill.csv'
output_file = 'your_path/output.csv'
main(input_file, output_file)
```

## China Merchants Bank Credit Bill to MoneyWize
### Function
- convert the bill from China Merchants Bank Credit to MoneyWiz CSV format

### How ot Use
1. download the bill from China Merchants Bank Credit, which is a PDF file
2. download [Tabula](https://tabula.technology/), which is a tool to convert PDF to CSV
3. convert the PDF to CSV, and save it as ```cmb_credit_bill.csv```
   1. This process might encounter recognition errors. Switching modes back and forth and trying multiple times should work.
   2. Also, pay attention to whether the automatically recognized table range is correct. If it's not, you can adjust it manually.
4. install the Python 3.10 environment
5. activate the Python 3.10 virtualenv ```source venv/bin/activate```
6. run
```pip install -r requirements.txt```
7. Run script

```python
from cmb_credit_converter import *
input_file = 'your_path/alipay_bill.csv'
output_file = 'your_path/output.csv'
main(input_file, output_file)
```

