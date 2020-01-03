#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 16:49
# @Author  : Z
# @Email   : S
# @File    : 1.0PCA.py
import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(X.shape)
pca = PCA(n_components=1)
pca.fit(X)
# PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
      # svd_solver='auto', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)  # doctest: +ELLIPSIS
    # [ 0.99244...  0.00755...]
print(pca.singular_values_)  # doctest: +ELLIPSIS
    # [ 6.30061...  0.54980...]