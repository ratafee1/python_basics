#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 17:08
# @Author  : Z
# @Email   : S
# @File    : 4.1figureDraw.py
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(224)

import  numpy as np
X = np.arange(10)
ax1.plot(X,X)
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("Y=X")
ax2.plot(X,-X)
ax3.plot(-X,X)
ax4.plot(-X,-X)

plt.show()

