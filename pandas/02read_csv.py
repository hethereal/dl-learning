"""
读取Excel文件
"""
import pandas as pd

data = pd.read_csv("./data/sales_data.csv", nrows = 20)

data2 = pd.read_csv("./data/sales_data.csv", skiprows = [i for i in range(1, 21)])

data3 = pd.read_csv("./data/sales_data.csv", skiprows = lambda x: x % 2 != 0)

data4 = pd.read_csv("./data/sales_data.csv", usecols = [0, 1, 2, 3, 4])

data5 = pd.read_csv("./data/sales_data.csv", usecols = ['date', 'customer_name'])

data6 = pd.read_csv("./data/sales_data.csv", index_col = 'order_id')

data7 = pd.read_csv("./data/sales_data.csv", usecols = [0], header = 0, names = ['订单ID'])

data8 = pd.read_csv("./data/sales_data.csv", chunksize = 10)
for chunk in data8:
    print(chunk)