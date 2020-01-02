#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:21
# @Author  : Z
# @Email   : S
# @File    : 14.0file.py
import pandas as pd
df_love=pd.read_csv("D:\PycharmProject\MachineLearning\day04\SklearnTest.txt")
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

train_data=df_love.query("is_date != -1")
print(train_data)
test_data=df_love.query("is_date == -1")
print(test_data)
df2=df_love.drop(labels="is_date",axis=1)
print(df2)
#    height  house  car  handsome  job
# 0    1.80      1    0       6.5    2
# 1    1.62      1    0       5.5    0
# 2    1.71      0    1       8.5    1
# 3    1.58      1    1       6.3    1
# 4    1.68      0    1       5.1    0
# 5    1.63      1    0       5.3    1
# 6    1.78      0    0       4.5    0
# 7    1.64      0    0       7.8    2
# 8    1.65      0    1       6.6    0