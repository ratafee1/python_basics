#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:43
# @Author  : Z
# @Email   : S
# @File    : 12.0if_elif_else.py
number=60
flag= False
while flag==False:
    #用户输入猜测数字
    guessNumber=input("Please input your guess Number:")
    #判断
    if guessNumber == number:
        print "Wow"
        print "Congratulations,you will win the whole world!"
        flag=True
    elif guessNumber >number:
        print "Guessnumer is larger than given one!"
    else:
        print "GuessNumber is smaller than given one"