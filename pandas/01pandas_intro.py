"""
Pandas入门
"""
import pandas as pd

df = pd.DataFrame({
    "name": ["张三", "李四"],
    "age": [18, 19],
    "sex": ["男", "女"],
})
print(df['age'].max())

print(df.describe())