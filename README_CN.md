# 支付宝账单转MoneyWiz
## 简介
这是一个简单的脚本，用于将支付宝账单转换为MoneyWiz的CSV格式。

## 功能
- 删除前4行的账户信息，只保留账单交易
- 删除空行
- 处理支付宝在csv中的不良格式，例如关于逗号和制表符的误用
- 添加“收”和“支”列，代表收入和支出，它适合MoneyWiz的CSV格式关于收入和支出

## 如何使用
1. 下载支付宝账单csv文件
2. 安装Python 3.10环境
3. 激活Python 3.10虚拟环境 ```source venv/bin/activate```
4. 运行
```pip install -r requirements.txt```
5. 运行脚本
```python
from main import *
input_file = 'your_path/alipay_bill.csv'
output_file = 'your_path/output.csv'
main(input_file, output_file)
```


