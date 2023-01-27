# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:16:46 2023

@author: drsau
"""

from tkinter import *
import random


root = Tk()
root.title("Sales Application")
root.geometry("400x400")


month = ("January","February","March","April","May","June","July","August","September","October","November","December")

profit = (740000,450000,7800,9700,120000,45600,650000,54000,1000000,3000,7000000,9000)

label_month = Label(root)
label_month["text"] = "Months : " + str(month)

label_profit = Label(root)
label_profit["text"] = "Profits : "+ str(profit)

label_min_profit = Label(root)
label_max_profit = Label(root)


def max_min_profit():
    max_profit = max(profit)
    max_profit_index = profit.index(max_profit)
    print(max_profit_index)

    max_profit_month  = month[max_profit_index]
    label_max_profit["text"] = "The maximum profit of "+ str(max_profit)+ " was recorded in the month of " + str(max_profit_month)

    min_profit = min(profit)
    min_profit_index = profit.index(min_profit)
    print(min_profit_index)

    min_profit_month = month[min_profit_index]
    label_min_profit["text"] = "The minimum profit of "+ str(min_profit)+" was recorded in the month of " + str(min_profit_month)


label_month.place(rely=0.3,relx=0.2)