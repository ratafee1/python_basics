#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 17:23
# @Author  : Z
# @Email   : S
# @File    : 7.0DataFrmae.py
import pandas as pd
import numpy as np
print(pd.DataFrame([1,2,3,4]))


print("*" *100)
print(pd.DataFrame([[1,2,3,4],[3,5,5,6]]))
print(pd.DataFrame(np.random.randn(5,5)))
#如何添加名字
df1 = pd.DataFrame([[1, 2, 3, 4], [3, 5, 5, 6]], columns=["Apple", "Pear", "Bnanana", "Orange"],
                     index=["a", "b"],dtype="float32")
print(df1)
print(df1.head(1))
print("\n"*100)
#属性数据有哪些
print(df1.index) #Index(['a', 'b'], dtype='object')
print(df1.columns) #Index(['Apple', 'Pear', 'Bnanana', 'Orange'], dtype='object')
print(df1.shape) #(2, 4)
print(df1.ndim) #2
print(df1.size) #8
print(df1.dtypes)


#取值
print(df1)
print("*"*100)
print(df1["Apple"])
# print(df1["a"])
#如果需要对行进行分析
print("*"*100)
print(df1.ix[:,"Apple"])
print(df1.ix["a","Apple"])
print("*"*100)
print(df1.ix["a":"b","Apple":"Bnanana"])
dict_data = {   'A': 1,
	             'B': pd.Timestamp('20170426'),
	             'C': pd.Series(1, index=list(range(4)),dtype='float32'),
	             'D': np.array([3] * 4,dtype='int32'),
	             'E': ["Python","Java","C++","C"],
	             'F': 'ITCast' }
#print dict_data
df_obj2 = pd.DataFrame(dict_data,index=["a","b","c","d"])
print(df_obj2)
#loc和iloc方法
print(df_obj2.iloc[:2])
print(df_obj2.iloc[0:3,0:3])
print(df_obj2.iloc[[0,1],[0,3]])
#通过loc查看样本数据
print(df_obj2.loc[["a","b"],["A","B"]])
print(df_obj2.loc["a","A"])
#增加数据
df1["Pen"]=df1["Apple"]*2
print(df1)
#删除数据列
del df1["Pen"]
print(df1)