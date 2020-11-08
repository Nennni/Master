#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:12:58 2020

@author: FrancescoIraci
"""
import numpy as np
import matplotlib.pyplot as plt

month,profit=np.genfromtxt("CompanySalesData.txt", dtype=float, comments="#" , usecols=(0,8), unpack=True)

a=plt.plot(month, profit, "r-")
plt.text(1.8, 2.0 ,fontsize=17)
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company profit per month")
plt.show()
