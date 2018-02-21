# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os;
print ('Hello World!')

#print the current working directory
print (os.getcwd())
#set working directory
path = "C://Users/madh9981/Documents/Learning/Udemy_ML/Part 1 - Data Preprocessing"
os.chdir(path);
# or just save the python file in the directory and hit F5 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv('Data.csv')

# the indes in python starts at 0(zero)

#formatting dataset
#3 to 0 and g to f for floating number

#creating the matrix
X = dataset.iloc[:, :-1].values
#object arrays are not supported error while viewing X in variable Explorer so df is created
df = pd.DataFrame(X)
# first colon-> take all the lines and :-1 is take all the columns except the last one
#y = dataset.iloc[:, :3].values # this will import 3 colomns 1,2,3 not 0,1,2
y = dataset.iloc[:, 3] #this will import only the third column starting from 0 not 1(index starts with 0)
dy = pd.DataFrame(y)

#handling missing data with mean
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
#the upper bound is excluded so to take column 1 and 2 1:3 is written remember: index starts with 0 in python
X[:, 1:3] = imputer.transform(X[:, 1:3])




