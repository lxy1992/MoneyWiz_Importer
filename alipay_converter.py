import pandas as pd


def process_csv(input_file, output_file):
    # 读取CSV文件，跳过前4行
    df = pd.read_csv(input_file, skiprows=4, encoding='GBK')

    # 重命名列，包括额外的列
    columns = ['交易号', '商家订单号', '交易创建时间', '付款时间', '最近修改时间', '交易来源地', '类型',
               '交易对方', '商品名称', '金额（元）', '收/支', '交易状态', '服务费（元）', '成功退款（元）', '备注', '资金状态', '额外列']
    df.columns = columns

    # 删除不需要的列
    df.drop(columns=['商家订单号', '最近修改时间', '交易来源地', '额外列'], inplace=True)

    # 确保 '金额（元）' 和 '收/支' 列是字符串类型，并去除空格
    df['金额（元）'] = df['金额（元）'].astype(str).str.strip().astype(float)
    df['收/支'] = df['收/支'].astype(str).str.strip()

    # 根据 '收/支' 列创建 '支出' 和 '收入' 列
    df['支出'] = df.apply(lambda row: row['金额（元）'] if row['收/支'] == '支出' else 0, axis=1)
    df['收入'] = df.apply(lambda row: row['金额（元）'] if row['收/支'] == '收入' or row['收/支'] == '不计收支' else 0, axis=1)

    # 保存为新的CSV文件
    df.to_csv(output_file, index=False)


def main(input_file, output_file):
    process_csv(input_file, output_file)
