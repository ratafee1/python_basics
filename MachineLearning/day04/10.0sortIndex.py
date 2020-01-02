#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 18:03
# @Author  : Z
# @Email   : S
# @File    : 10.0sortIndex.py
# DataFrame
import numpy as np
import pandas as pd
df4 = pd.DataFrame(np.random.randn(3, 5),
		                   index=np.random.randint(3, size=3),
		                   columns=np.random.randint(5, size=5))
print(df4)

df4_isort = df4.sort_index(axis=1, ascending=False)
print(df4_isort) # 4 2 1 1 0