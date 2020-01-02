#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:05
# @Author  : Z
# @Email   : S
# @File    : 11.0sortIndex2.py
import numpy as np
import pandas as pd
s1=pd.Series(np.random.randn(12),index=[
    ["a","a","a","b","b","b","c","c","c","d","d","d"],[0,1,2,0,1,2,0,1,2,0,1,2]
])
print(s1)
#访问外层索引的值
print(s1["a"])
print(s1["a",1])
print(s1[:,1])
#交换内外层索引
print(s1.swaplevel())
print(s1.swaplevel().sortlevel())

print(s1.index)
# MultiIndex(levels=[['a', 'b', 'c', 'd'], [0, 1, 2]],
#            labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]])
