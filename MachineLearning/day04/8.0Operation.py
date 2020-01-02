#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 17:50
# @Author  : Z
# @Email   : S
# @File    : 8.0Operation.py
import pandas as pd
s1=pd.Series(range(10),index=range(10))
s2=pd.Series(range(5),index=range(5))
print("S1:",s1)
print("S2:",s2)
print("S1+S2:",s1+s2)
# print(s1.add(s2,fill_value=100))
import numpy as np
df1=pd.DataFrame(np.ones((3,3)),columns=["a","b","c"])
df2=pd.DataFrame(np.ones((2,2)),columns=["a","b"])
print(df1+df2)
print(df1.add(df2,fill_value=100))