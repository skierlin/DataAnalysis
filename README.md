# DataAnalysis

## numpy

### numpy 创建数组

- array(x) : 根据列表或者元组x创建数组
- arange(x) : 创建一维数组，元素等价range(x,y,i)
- linespace(x,y,n): 创建一个由区间[x, y]的n-1等分点构成的一维数组
- random.randint(...): 创建一个元素为随机整数的数组
- zeros(n) : 创建一个长度全为0的长度n数组
- ones(n) : 创建一个元素全为1的长度为n的数组

### 数组常用属性和函数

- dtype ： 数组元素的类型
- ndim  :  数组维度
- shape ： 数组每维的长度
- size  ： 数组元素个数
- argwhere(...) : 查找元素
- tolist() : 转换为list
- min() : 求最小元素
- max() : 求最大元素
- reshape(...) : 改变数组的形状
- flatten() : 转换为一维数组

### 数组元素增删

- append(x,y) 若y是数组，列表，元组，就将y的元素添加进数组x得到新的数组，否则将y本身添加进数组x得新数组
- concatenate(...) 拼接多个数组或列表
- delete(...) 删除数组元素得新数组

numpy数组一旦生成，元素就不能增删，会返回一个新的数组

### 查找元素

- argwhere(n) 查找所有n在的索引，不限于一维

### 数学运算

- `+1`: 所有元素加
- `a*b`: 对应元素相乘
- `a+b`: 对应元素相加
- sqrt： 开方

### numpy 切片

numpy的切片是原数组的一部分，而非一部分的拷贝

## pandas

### Series

增删查改

增
- 直接新建，或者append

删
- pop

### DataFrame

#### dataframe的构造和访问


#### dataframe的切片与统计

- iloc[行选择器, 列选择器] 用下标做切片
- loc[行选择器, 列选择器] 用标签做切片

#### 分析统计
- df.T : 转置矩阵
- df.sort_values('语文',ascending=False) # #按语文成绩降序排列
- df.sum()['语文'] 
- df.mean()['数学']
- df.median()['英语']
- df.min()['语文']
- df.max()['数学']


#### 修改和增删

- df.insert
- df.drop
