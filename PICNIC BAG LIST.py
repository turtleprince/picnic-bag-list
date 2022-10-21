# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:01:59 2022

@author: turtl_4
"""

from tkinter import *
import random
root = Tk()
root.title("PICNIC BAG LIST")
root.geometry("400x400")

r_num_list = Label(root)
r_num_sorted_list = Label(root)


list=["Bottle", "Tiffen", "ID card", "chocolates", "Chips", "Tickets", "Hanky"]

def picnic_bag_list():
    r_num = random.randint(0, 5)
    print(r_num)
    print("Your Picnic Bag Iteam Is: "+list[r_num])



btn = Button(root,text="what will you chose to put in your picnic bag",command=picnic_bag_list)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()