#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 16:33
# @Author  : Z
# @Email   : S
# @File    : 5.0NumpyMatrixOperation.py
import numpy as np
arr1=np.array([[1,2],[3,4]]) #2*2
arr2=np.array([[1,2],[3,4]]) #2*2
#矩阵的乘法-第一个矩阵的列的维度和第二个矩阵的行的维度必须一致
print(arr1.dot(arr2))
print(np.dot(arr1,arr2))
#矩阵的行列式
from numpy.linalg import det,inv,qr,eig,svd
print("arr1 matrix values is:",det(arr1))
#矩阵的逆-存在的条件是矩阵的行列式不为0
print("arr1 inverse values is:",inv(arr1))
arr2 = np.array([[1, 2], [2, 4]])
print("arr2 det values:",det(arr2))
# print("arr2 inverse values is:",inv(arr2)) #numpy.linalg.linalg.LinAlgError: Singular matrix
#矩阵的分解---qr分解---将矩阵分解为q矩阵和r矩阵
q,r=qr(arr1)
print(q)
print(r)
# [[-0.31622777 -0.9486833 ]
#  [-0.9486833   0.31622777]]
# [[-3.16227766 -4.42718872]
#  [ 0.         -0.63245553]]
print(np.dot(q,r))
# [[1. 2.]
#  [3. 4.]]
# 特征值和特征向量分解-------PCA
eigenvalues,eigenvectors=eig(arr1)
print("values:",eigenvalues)
print("Vec:",eigenvectors)
#还原
print(np.dot(eigenvectors,np.dot(np.diag(eigenvalues),inv(eigenvectors))))
# [[1. 2.]
#  [3. 4.]]
# 奇异值分解 svd
U,Sigma,VT=svd(arr1)
print("U:",U)
print("Sigma:",Sigma)
print("VT:",VT)
#还原
print(np.dot(U,np.dot(np.diag(Sigma),VT)))
