#-*- coding: utf-8 -*-
# @Time    : 2018/9/28 17:43
# @Author  : Z
# @Email   : S
# @File    : 14.1exception_if_elif_else.py
import tkinter.simpledialog as dl
import tkinter.messagebox as mb
mb.showinfo("Welcome", "Welcome to Guess Number Game")
number=60
while True:
    #用户输入猜测数字
    guessNumber=dl.askinteger("GuessGame","Please input your guess Number:")
    #判断
    if guessNumber == number:
        mb.showinfo("Wow","Congratulations,you will win the whole world!")
        break
    elif guessNumber >number:
        mb.showinfo("losser","Guessnumer is larger than given one!")
        continue
    else:
        mb.showinfo("losser","GuessNumber is smaller than given one")
        continue
