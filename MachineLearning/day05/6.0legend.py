#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 17:39
# @Author  : Z
# @Email   : S
# @File    : 6.0legend.py
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(1,10,1000)
y1=X
plt.plot(X,y1,label=["Y=x"])
y2=X**2
plt.plot(X,y2,label=["Y=X**2"])
y3=X**3
plt.plot(X,y3,label=["Y=X**3"])
#使用loc=0默认是“best”,1-4分别是不同位置，ncol是列
plt.legend(loc="best",ncol=2)

plt.show()