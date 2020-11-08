#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:17:58 2020

@author: FrancescoIraci
"""

from ReadProducts import *

import matplotlib.pyplot as plt

fname="CompanySalesData.txt"
N=12

(month,facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer)=readfast(fname,N)


a=plt.plot(month, facecream, "r-o", label="Profit data of last year")
b=plt.plot(month, facewash, "o-o", label="Profit data of last year")
c=plt.plot(month, toothpaste, "b-o", label="Profit data of last year")
d=plt.plot(month, bathingsoap, "g-o", label="Profit data of last year")
e=plt.plot(month, shampoo, "p-o", label="Profit data of last year")
f=plt.plot(month, moisturizer, "y-o", label="Profit data of last year")

plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Company profit per month")
plt.legend(loc='lower right')
plt.show()