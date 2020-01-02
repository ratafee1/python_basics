# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 17:56
# @Author  : Z
# @Email   : S
# @File    : 9.0PandasFunction.py
import numpy as np
import pandas as pd

df_data = pd.DataFrame([np.random.randn(3), [1., 2., np.nan],
                        [np.nan, 4., np.nan], [1., 2., 3.]])
# print(df_data.head())
# # is_null
# print(df_data.isnull())
# # dropna
# df2 = df_data.dropna(axis=0) #行
# df3 = df_data.dropna(axis=1) #列
# print(df2)
# print(df3)
# fillna
df4=df_data.fillna(100)
print(df4)
# abs--直接使用numpy函数
print(np.abs(df_data))
# apply
print(df4.apply(lambda x:x.max(),axis=1))
