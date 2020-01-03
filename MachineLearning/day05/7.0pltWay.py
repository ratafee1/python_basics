#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 17:52
# @Author  : Z
# @Email   : S
# @File    : 7.0pltWay.py

import matplotlib.pyplot as plt
import  numpy as np
X=np.linspace(1,10,100)
ax1=plt.subplot(221)
plt.sca(ax1)
plt.plot(X,np.sin(X),"r--",label=["Y=sin(X)"])
plt.legend(loc=0)
plt.title("Y=sin(X)")













plt.subplot(222)
X1=np.linspace(-10,10,100)
plt.plot(X1,np.tanh(X1),"b-.",marker="o",label=["Y=tanh(X)"])
plt.ylim(-1,1)
plt.xlim(-10,10)
plt.legend(loc="best")
plt.grid()

plt.subplot(212)
plt.plot(X1,np.sign(X1),linestyle="-",linewidth=2,color="red")
plt.show()