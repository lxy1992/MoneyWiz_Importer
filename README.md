# Alipay Bill To MoneyWiz  
- [中文文档](https://github.com/lxy1992/alipay_moneywiz_importer/blob/master/README_CN.md)
## Introduction
This is a simple script to convert Alipay bill to MoneyWiz CSV format.

## Function
- remove the first 4 line about account info, only keep the bill transactions
- remove empty lines
- process alipay bad format in csv, such as misuse about comma and tab
- add 收 and 支 columns, which represent income and expense, it fits MoneyWiz's CSV format about income and expense

## How to Use
1. download the alipay bill csv file
2. install the Python 3.10 environment
3. activate the Python 3.10 virtualenv ```source venv/bin/activate```
4. run
```pip install -r requirements.txt```
5. Run script
```python
from main import *
input_file = 'your_path/alipay_bill.csv'
output_file = 'your_path/output.csv'
main(input_file, output_file)
```