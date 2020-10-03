# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:25:19 2019

@author: Mr.zhang
"""

import turtle as t
t.pensize(4)
t.penup()
t.goto(10,20)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(30,steps=4)
t.end_fill()
t.done()