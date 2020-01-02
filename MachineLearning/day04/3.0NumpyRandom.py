#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 15:28
# @Author  : Z
# @Email   : S
# @File    : 3.0NumpyRandom.py
import numpy as np
n1=np.random.random((4,5))
print(n1)
n2=np.random.randn(4,4)
print(n2)
n3=np.random.uniform(0,1,size=(3,3))
print(n3)
n4=np.random.chisquare(10,size=(4,4))
print(n4)
n5=np.random.binomial(10,0.4,size=(4,4))
print(n5)
# [[2 7 4 4]
#  [4 5 7 4]
#  [4 5 5 5]
#  [2 4 5 4]]