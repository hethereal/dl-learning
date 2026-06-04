"""
创建DataFrame
"""
import pandas as pd

# 通过列表创建
l = [1, 2, 3]
df = pd.DataFrame(l, columns=['num'])
print(df)

# 通过嵌套列表
l = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(l, columns=['num1', 'num2', 'num3'])
print(df)

# 通过字典创建
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)

# 指定索引
l = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(l, index=['a', 'b'], columns=['num1', 'num2', 'num3'])
print(df)

# 通过字典列表创建
d = [
    {
        "one": 1.0,
        "two": 2.0,
        "three": 3.0
    },
    {
        "one": 4.0,
        "two": 5.0,
        "three": 6.0
    }
]
df = pd.DataFrame(d)
print(df)