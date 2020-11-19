#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:52:43 2020

@author: FrancescoIraci
"""

from ReadProfit import *

import matplotlib.pyplot as plt

fname="CompanySalesData.txt"
N=12

(month,facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer)=readfast(fname,N)
print(month,facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer)

a=plt.plot(month, facecream, marker="o", label="Face cream sales data")
b=plt.plot(month, facewash, marker="o", label="Face wash sales data")
c=plt.plot(month, toothpaste, marker="o", label="Toothpaste sales data")
d=plt.plot(month, bathingsoap, marker="o", label="Bathingsoap sales data")
e=plt.plot(month, shampoo, marker="o", label="Shampoo sales data")
f=plt.plot(month, moisturizer, marker="o", label="Moisturizer sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number ")
plt.title("Sales data")
plt.legend(loc='upper left')
plt.show()
