# MoneyWiz 导入工具

## 简介
这是一个脚本集，包含：
- 支付宝账单转 MoneyWiz，将支付宝账单转换为 MoneyWiz CSV 格式。
- 中国招商银行信用卡账单转 MoneyWiz，将招商银行信用卡账单转换为 MoneyWiz CSV 格式。

## 支付宝账单转 MoneyWiz
### 功能
- 删除前四行关于账户信息，只保留账单交易
- 删除空行
- 处理支付宝在 csv 中的错误格式，例如关于逗号和制表符的误用
- 添加 “收” 和 “支” 列，代表收入和支出，它符合 MoneyWiz 的 CSV 格式的收入和支出

### 使用方法
1. 下载支付宝账单 csv 文件
2. 安装 Python 3.10 环境
3. 激活 Python 3.10 虚拟环境 ```source venv/bin/activate```
4. 运行
```pip install -r requirements.txt```
5. 运行脚本

```python
from alipay_converter import *

input_file = '你的路径/alipay_bill.csv'
output_file = '你的路径/output.csv'
main(input_file, output_file)
```

## 中国招商银行信用卡账单转 MoneyWiz
### 功能
- 将招商银行信用卡账单转换为 MoneyWiz CSV 格式

### 使用方法
1. 从招商银行信用卡下载账单，它是一个 PDF 文件
2. 下载 [Tabula](https://tabula.technology/)，这是一个将 PDF 转换为 CSV 的工具
3. 将 PDF 转换为 CSV，并将其保存为 ```cmb_credit_bill.csv```
   1. 这个过程可能会出现识别错误的情况，来回切换模式，多试几次，会可以的
   2. 还有要注意它自动识别的表格范围对不对，不对的话，可以手动调整
4. 安装 Python 3.10 环境
5. 激活 Python 3.10 虚拟环境 ```source venv/bin/activate```
6. 运行
```pip install -r requirements.txt```
7. 运行脚本

```python
from cmb_credit_converter import *
input_file = '你的路径/cmb_credit_bill.csv'
output_file = '你的路径/output.csv'
main(input_file, output_file)
```