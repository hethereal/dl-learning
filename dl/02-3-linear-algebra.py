"""
线性代数
"""
import torch

# 标量
x = torch.tensor(3.0)
y = torch.tensor(2.0)
print(x + y, x * y, x / y, x ** y) # tensor(5.) tensor(6.) tensor(1.5000) tensor(9.)

# 向量
x = torch.arange(4)
print(x)

y = x[3]
print(y)

l = len(x)
print(l)

# 矩阵
A = torch.arange(20).reshape(5, 4)
print(A)

# 矩阵转置
print(A.T)

# 求和
x = torch.arange(4, dtype=torch.float32)
print(x.sum())

# 降维
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A.sum(axis=0), A.sum(axis=1), A.sum())

# 平均值
print(A.mean(), A.sum() / A.numel())

print(A.mean(axis=0))

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A.sum(axis=1, keepdim=True))

# 点积
x = torch.arange(4, dtype=torch.float32)
y = torch.ones(4, dtype=torch.float32)
print(torch.dot(x, y))
print(torch.sum(x * y))
