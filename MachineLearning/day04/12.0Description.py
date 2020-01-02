#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:11
# @Author  : Z
# @Email   : S
# @File    : 12.0Description.py
import  pandas as pd
import  numpy as np

df1 = pd.DataFrame(np.random.randn(5, 4), columns=["a", "b", "c", "d"])
print(df1)

# sum, mean, max, min…
# 		axis=0 按列统计，axis=1按行统计
# 		skipna 排除缺失值， 默认为True
print(df1.sum(axis=0)) #按列统计
print(df1.sum(axis=1)) #axis=1按行统计
print(df1.mean(axis=0))
print(df1.mean(axis=1))
print(df1.std(axis=0))
print(df1.std(axis=1))

#decsription
print(df1.describe())
#               a         b         c         d
# count  5.000000  5.000000  5.000000  5.000000
# mean  -0.609401  0.362187  0.308309  0.792321
# std    1.724866  0.847899  0.522396  0.935367
# min   -2.046074 -0.421151 -0.260338 -0.145751
# 25%   -1.864597 -0.358164  0.040752  0.095148
# 50%   -0.756256  0.304962  0.063671  0.525143
# 75%   -0.640965  0.631912  0.686425  1.388126
# max    2.260885  1.653379  1.011035  2.098937
