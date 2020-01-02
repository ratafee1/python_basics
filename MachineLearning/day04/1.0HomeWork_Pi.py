#-*- coding: utf-8 -*-
# @Time    : 2018/9/29 14:54
# @Author  : Z
# @Email   : S
# @File    : 1.0HomeWork_Pi.py
import  random
def estimatePi(times):#表示的是落入正方形的次数
    hists=0#落入圆内次数
    for i in range(times):
        x=random.random()*2-1 #[0, 1)*2-1
        y=random.random()*2-1 #[0, 1)*2-1
        if x*x + y*y <=1:
            hists+=1
    return 4.0*hists/times

if __name__=="__main__":
    result=estimatePi(10000)
    print(result)