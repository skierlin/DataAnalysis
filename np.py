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

# 在数组中查找元素

a = np.array((1,2,3,5,3,4))
pos = np.argwhere(a==3)
print(pos)  #[[2] [4]]
a = np.array([[1,2,3], [4,5,2]])
pos = np.argwhere(a==2)
print(pos) #[[0 1] [1 2]]

# 抽取a中大于2的元素形成一个一维数组
b = a[a>2]
print(b)  #[3 4 5]
a[a > 2] = -1   #[[1 2 -1] [-1 -1 2]]



# 数学运算

a = np.array((1,2,3,4))
b = a+1  # [2 3 4 5]
print(b)
print(a*b) # [2 6 12 20]
print(a+b) # [3 5 7 9]
c = np.sqrt(a*10)  #[10 20 30 40]
print(c)


print("--------------------------")
print("数组切片")
# 数组切片

a = np.arange(8)
b = a[3:6] # b是a的一部分
print(b)
c = np.copy(a[3:6]) #c是a的一部分的拷贝
b[0] = 100
print(a)   #a的值会改变
print(c)   #c的值不会变化
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b = a[1:3, 1:4]



