#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 16:30
# @Author  : Z
# @Email   : S
# @File    : 5.0set.py
#集合-确定性、无序性、唯一性
s1={12,3,4,5,4,5,6}
print s1
#集合的增加
s1.add("apple")
print s1
#集合的删除
s1.remove("apple")
print s1
#集合的更新
s1.update({1,2,3,4,5,56,7,100})
print s1
#集合的运算
a={1,2,3,4}
b={1,2,3,5}
#集合交 1,2,3,
print a&b
print a.intersection(b)
#集合并 1 2 3 3 4 5
print a|b
print a.union(b)
#差集 a-b=4   b-a=5
print a-b
print a.difference(b)
print b-a
print a|b