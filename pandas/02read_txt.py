"""
读取TXT文件
"""
import pandas as pd
data = pd.read_table("./data/sales_data.txt", encoding = "utf-8")

print(data)