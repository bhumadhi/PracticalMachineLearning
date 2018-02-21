# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:01:09 2018

@author: madh9981
"""
#selecting rows/lines
dataset[:3] #select first three columns i.e up to index 3 exclude upper vound 3
dataset[4:7] #column 4,5,6 i.e from index 4 to 6 exclude 7
dataset[3:] #everything from index 3 onward

# upper bound is excluded but lower bound is not excluded
dataset.ix[3]
dataset.iloc[:, 3] # take index 3 i.e 4th column
dataset.iloc[:, 1:3] # take from index 1 to 2, upper bound excluded
dataset.iloc[:, 3:] # take from index 3 onwards
dataset.iloc[:, :3] # up to 2nd index, upper bound excluded

dataset.ix[:, 1:3] # take from index 3 onwards

dataset[:3]['Age'] # first 3 lines onwards and column 'Age'



