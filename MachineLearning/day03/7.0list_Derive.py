#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:39
# @Author  : Z
# @Email   : S
# @File    : 7.0list_Derive.py
#列表表达式-求解满足条件的列表-仍然是列表
#语法：[表达式 for 变量 in 可迭代对象中 if 条件]
#实践：x*x
print [x*x for x in range(10)]
#实践1：#1.使用列表推到式实现嵌套列表的平铺（两个for循环）
vec=[[1,2,3],[4,5,6],[7,8,9]]  # 1,2,3,4,5,5,6.....
#使用列表推导式
print [num for elem in vec for num in elem]
#等价于
result1=[]
for elem in vec:
    for num in elem:
        result1.append(num)
print result1
#实践2：过滤不符合条件的元素
arr=[1,2,3,4,0,-1,-3,-100,100]
print [x for x in arr if x>0]
#等价
result2=[]
for x in arr:
    if x>0:
        result2.append(x)
print result2

#实践3：列表推导中使用多个循环实现多序列元素任意的组合，并过滤元素
print [(x,y) for x in range(10) for y in range(10) if x!=y]
result3=[]
for x in range(10):
    for y in range(10):
        if x!=y:
            result3.append((x,y))
print result3
#实践4：实现列表推到式实现矩阵转置
vec=[[1,2,3],[4,5,6],[7,8,9]]  # 1,2,3,4,5,5,6.....
print [[row[i] for row in vec ]for i in range(3)]
#zip函数
# t1=zip([1,2,3],[4,5,6],[7,8,9])
t1=zip(*vec) #[1,2,3],[4,5,6],[7,8,9]
print map(list,t1)
# print zip([[1,2,3],[4,5,6],[7,8,9]])

#实践5：使用列表推导生成100以内的所有素数
#素数-除了1和本身不能被其他数整除的
print [p for p in range(2,101) if 0 not in [p%q for q in range(2,p)]]
# import numpy as np
# print [p for p in range(2,101) if 0 not in [p%q for q in range(2,int(np.sqrt(p))+1)]]
