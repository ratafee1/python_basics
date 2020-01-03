#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 16:58
# @Author  : Z
# @Email   : S
# @File    : 3.0matDeno2.py
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(1,10)
#y=5+x
y=5+X
plt.plot(X,y)
#y=5+2*x
y1=5+2*X
plt.plot(X,y1)
plt.title(u"This is 函数 y=x!",fontproperties="SimHei")
plt.xlabel("X")
plt.ylabel("Y")
#显示
plt.show()