"""
数据操作-入门
"""
import torch
from numpy.ma.core import reshape

x = torch.arange(12)

print(x.shape)
print(x.numel())

x = x.reshape(3, 4)
print(x)

x = torch.zeros((2, 3, 4))
print(x)
x = torch.ones((2, 3, 4))
print(x)
x = torch.randn((2, 3, 4))
print(x)

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
print(x ** y)

print(torch.cat((x, y), dim=0))

x = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(x.sum())

# 广播
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a + b)

# 为结果分配新的内存空间
before = id(a)
print(before)
a = a + b
print(id(a))

# 原地操作
z = torch.zeros_like(a)
print("before: ", id(z))
z[:] = a + b
print("after: ", id(z))

before = id(a)
print("before: ", before)
a += b
print("after: ", id(a))

# 转换为其他Python对象
n = a.numpy()
m = torch.tensor(n)
print("n: ", n)
print("m: ", m)