# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:20:28 2016

@author: mikebaldwin
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics

data_file = open("catsM.csv", "r");

#create an empty list to store the data
data_list = [];
#put all lines from the file into a list
for ii in data_file:
    data_list.append(ii[3]);
    
#remove the first element (column header)
del data_list[0];
    
print(data_list)
