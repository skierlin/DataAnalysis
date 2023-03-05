import pandas as pd

# Series介绍

s = pd.Series(data=[80,90,100], index=['语文', '数学', '英语'])
for x in s:
    print(x, end=" ")
print()
print(s['语文'], s[1]) # 标签和序号都可以作为下标来访问元素
print(s[0:2]['数学'])  # s[0:2]是切片
print(s['数学':'英语'][1])
for i in range(len(s.index)):
    print(s.index[i], end=" ")
s['体育'] = 110 #在尾部添加元素，标签为'体育'，值为110
s.pop('数学') #删除标签为'数学’的元素
s2 = s.append(pd.Series(120, index = ['政治'])) #不改变s
print(s2['语文'],s2['政治']) #>>80 120
print(list(s2)) #>>[80, 100, 110, 120]
print(s.sum(),s.min(),s.mean(),s.median())
print(s.idxmax(),s.argmax())

# DataFrame的构造和访问

pd.set_option('display.unicode.east_asian_width',True)
#输出对齐方面的设置
scores = [['男',108,115,97],['女',115,87,105],['女',100,60,130],
['男',112,80,50]]
names = ['刘一哥','王二姐','张三妹','李四弟']
courses = ['性别','语文','数学','英语']
df = pd.DataFrame(data=scores,index = names,columns = courses)
print(df)

print(df.values[0][1],type(df.values))#>>108 <class 'numpy.ndarray'>
print(list(df.index)) #>>['刘一哥', '王二姐', '张三妹', '李四弟']
print(list(df.columns)) #>>['性别', '语文', '数学', '英语']
print(df.index[2], df.columns[2]) #>>张三妹 数学
s1 = df['语文'] #s1是个Series，代表'语文'那一列
print(s1['刘一哥'],s1[0]) #>>108 108 刘一哥语文成绩
print(df['语文']['刘一哥']) #>>108 列索引先写
s2 = df.loc['王二姐'] #s2也是个Series，代表“王二姐”那一行
print(s2['性别'],s2['语文'],s2[2])
#>>女 115 87 王二姐的性别、语文和数学分数


print("-------------------------------------")
print("切片和统计")

df2 = df.iloc[1:3, 1:3] #行切片，是视图，选1,2两行
print(df2)
df2 = df.loc['王二姐':'张三妹', '语文':'数学'] #和上一行等价
print(df2)

#        性别  语文  数学  英语
# 王二姐   女   115    87   105
# 张三妹   女   100    60   130

df2 = df.iloc[:2,[1,3]]
df2 = df.loc[:'王二姐',['语文','英语']] #和上一行等价
print(df2)

#         语文  英语
# 刘一哥   108    97
# 王二姐   115   105

df2 = df.iloc[[1,3],2:4]
df2 = df.loc[['王二姐','李四弟'],'数学':'英语'] #和上一行等价
print(df2)

#         数学  英语
# 王二姐    87   105
# 李四弟    80    50


print("---下面是DataFrame的分析和统计---")
print(df.T) #df.T是df的转置矩阵,即行列互换的矩阵
print(df.sort_values('语文',ascending=False)) #按语文成绩降序排列
print(df.sum()['语文'],df.mean()['数学'],df.median()['英语'])
#>>435 85.5 101.0 语文分数之和、数学平均分、英语中位数
print(df.min()['语文'],df.max()['数学'])
#>>100 115 语文最低分，数学最高分
print(df.max(axis = 1)['王二姐']) #>>115 王二姐的最高分科目的分数
print(df['语文'].idxmax()) #>>王二姐 语文最高分所在行的标签
print(df['数学'].argmin()) #>>2 数学最低分所在行的行号
print(df.loc[(df['语文'] > 100) & (df['数学'] >= 85)])


print("---下面是DataFrame的增删和修改---")
df.loc['王二姐','英语'] = df.iloc[0,1] = 150 #修改王二姐英语和刘一哥语文成绩
df['物理'] = [80,70,90,100] #为所有人添加物理成绩这一列
df.insert(1,"体育",[89,77,76,45]) #为所有人插入体育成绩到第1列
df.loc['李四弟'] = ['男',100,100,100,100,100] #修改李四弟全部信息
df.loc[:,'语文'] = [20,20,20,20] #修改所有人语文成绩
df.loc['钱五叔'] = ['男',100,100,100,100,100] #加一行
df.loc[:,'英语'] += 10 #>>所有人英语加10分
df.columns = ['性别','体育','语文','数学','English','物理'] #改列标签
print(df)

df.drop( ['体育','物理'],axis=1, inplace=True) #删除体育和物理成绩
df.drop( '王二姐',axis = 0, inplace=True) #删除 王二姐那一行
print(df)

df.drop([df.index[i] for i in range(1,3)],axis=0,inplace = True)
#删除第1,2行
df.drop([df.columns[i] for i in range(3)],axis = 1,inplace =
True) #删除第0到2列























































































































































































