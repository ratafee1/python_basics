#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:21
# @Author  : Z
# @Email   : S
# @File    : 14.0file.py
import pandas as pd
df_love=pd.read_csv("MachineLearning/day04/SklearnTestTSV.txt",sep="\t")
print(df_love)
# read_csv = _make_parser_function('read_csv', sep=',')
# read_csv = Appender(_read_csv_doc)(read_csv)
#
# read_table = _make_parser_function('read_table', sep='\t')
# read_table = Appender(_read_table_doc)(read_table)
#属性
print(df_love.shape) #(9, 6)
print(df_love.ndim) #2
print(df_love.size) #54
print(df_love.dtypes)
# height      float64
# house         int64
# car           int64
# handsome    float64
# job           int64
# is_date       int64
print(df_love.info())
# RangeIndex: 9 entries, 0 to 8
# Data columns (total 6 columns):
# height      9 non-null float64
# house       9 non-null int64
# car         9 non-null int64
# handsome    9 non-null float64
# job         9 non-null int64
# is_date     9 non-null int64
# dtypes: float64(2), int64(4)
# memory usage: 512.0 bytes

