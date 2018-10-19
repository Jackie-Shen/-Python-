import numpy as np

x = np.array([0, 1]) #输入
w = np.array([0.5, 0.5]) #权重
b = -0.7 #偏置

print(np.sum(x*w) + b)