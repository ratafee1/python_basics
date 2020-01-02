#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:16
# @Author  : Z
# @Email   : S
# @File    : 13.0query.py
from numpy.random import randn
from pandas import DataFrame
df = DataFrame(randn(10, 2), columns=list('ab'))#【“a”,"b"】
print(df)
print(df.query('a > b'))
print(df[df.a > df.b])