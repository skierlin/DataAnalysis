import numpy as np

# 初始化相关
# print(np.array([1, 2, 3]))
# print(np.arange(1, 9, 2))
# print(np.linspace(1, 10, 4))
# print(np.random.randint(10, 20, [2, 3]))
# print(np.random.randint(10, 20 ,5))
# a = np.zeros(3)
# print(a)
# print(list(a))
# a = np.zeros((2, 3), dtype=int)
# print(a)


# 常见属性和函数
# b = np.array([i for i in range(12)])
# print(b)
# a = b.reshape((3, 4))
# print(a)
# print(len(a))
# print(a.size)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# L = a.tolist()
# print(L)
#
# b = a.flatten()
# print(b)

### 增加新的元素

# a = np.array((1,2,3))
# b = np.append(a, 10)
# print(b)
# print(np.append(a, [10,20]))
# c = np.zeros((2,3), dtype=int)
# print(np.append(a, c))
# print(np.concatenate((a, [10, 20], a)))
# print(np.concatenate((c, np.concatenate((c, np.array([[10, 20, 30]]))))))
# print(np.concatenate((c, np.array([[1,2],[10,20]])), axis=1))


# 删除数组元素

a = np.array((1,2,3,4))
# 删除a中下标为1的元素
b = np.delete(a, 1)
print(b)

b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(np.delete(b, 1, axis=0))     # 删除b的第一行
print(np.delete(b, 1,axis=1))      # 删除b的第一列
print(np.delete(b, [1,2], axis=0)) # 删除b的第1行和第2行
print(np.delete(b, [1,3], axis=1)) # 删除b的第1列和第3列



