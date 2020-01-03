#-*- coding: utf-8 -*-
# @Time    : 2018/10/8 17:03
# @Author  : Z
# @Email   : S
# @File    : 4.0figure.py
import matplotlib.pyplot as plt
#多图创建
fig1=plt.figure()
#子图创建
fig1.add_subplot(121) #第一个参数表示的是：第几行，第二额参数：第几列，第三个参数表示：第几幅图
fig1.add_subplot(222) #第一个参数表示的是：第几行，第二额参数：第几列，第三个参数表示：第几幅图
fig1.add_subplot(223) #第一个参数表示的是：第几行，第二额参数：第几列，第三个参数表示：第几幅图
fig1.add_subplot(224) #第一个参数表示的是：第几行，第二额参数：第几列，第三个参数表示：第几幅图

fig2=plt.figure()
fig2.add_subplot(1,1,1)

plt.show()
