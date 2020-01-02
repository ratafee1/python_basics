# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 15:44
# @Author  : Z
# @Email   : S
# @File    : 4.0numpyArray.py
import numpy as np
#进一步学习矩阵或数组的创建
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array((1, 2, 3, 4))
arr3 = np.array({1, 2, 3, 4})
print(arr1)
print(arr2)
print(arr3)
print(type(arr3))
#属性ndim-shape-size
print(arr1.ndim) #1
print(arr1.shape) #(4,)
print(arr1.size) #4
#二维度矩阵
arr4=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(arr4)
# [[1 2 3]
#  [3 4 5]
#  [4 5 6]]
print(arr4.ndim) #2
print(arr4.shape) #3 3
print(arr4.size) #3*3=9
#三维度
arr5=np.array([[[1,2],[3,4],[5,6]]],dtype="float32")
print(arr5)
print(arr5.ndim) #3
#全为0矩阵
print(np.zeros(shape=(3,3)))
#全为1矩阵
print(np.ones(shape=(3,3)))
#等差数列
print(np.linspace(1,10,10))
#等比数列
print(np.logspace(1,10,10))
#对角阵
print(np.diag([1,2,3]))