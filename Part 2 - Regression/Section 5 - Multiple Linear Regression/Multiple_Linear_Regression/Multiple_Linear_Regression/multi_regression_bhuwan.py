# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:38:27 2018

@author: madh9981
"""

import os 
    print (os.name)  
    #print the current working directory
    print (os.getcwd())
    #set working directory
    loc = "C:/Users/madh9981/Documents/Learning/Udemy_ML/Part 2 - Regression/Section 5 - Multiple Linear Regression/Multiple_Linear_Regression/Multiple_Linear_Regression"
    os.chdir(loc);
    
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values #all columns except rightmost/last column
y = dataset.iloc[:, 4].values   #column 0 to 3(4 is not included)

#one hot encoder for categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#avoiding the dummy variable trap
X = X[:,1:] # removed the 1st column from X (start from index 1 and all others)
#not necessary here the python takes care of it

#split the training and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

#fitting multiple linear regression to train set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression() 
regressor.fit(X_train, y_train)

#predicting the test set results
y_pred = regressor.predict(X_test)

#building the optimal model using Backward Elimination
import statsmodels.formula.api as sm #does not take accont b0, so x0=1 is needed
#X = np.append(arr = X, values = np.ones((50,1)).astype(int),axis = 1)
#here array with value 1 will be append at last of X so we do the below instead of adding 1 to X, add X to 1s
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis =1)
#np.ones((50,1)).astype(int) remember the double (())

X_opt = X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
#see P>|t| column and see the hight value p value
#here x2 has highest p value(const, x1, x2,...)
X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

