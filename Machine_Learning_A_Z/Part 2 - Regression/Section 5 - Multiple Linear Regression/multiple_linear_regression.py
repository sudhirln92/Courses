#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:16:55 2018

@author: sudhir
"""

# =============================================================================
# 
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
#  Importing data
# =============================================================================
dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:,4].values
#y = dataset.loc[:,'Purchased'].values # Dependent variable
dataset.head()
dataset.tail()

# =============================================================================
# Encoding categorical data
# =============================================================================
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])

onehotendocer = OneHotEncoder(categorical_features= [3])
X = onehotendocer.fit_transform(X).toarray()

# Avoid dummy variable trape
X = X[:,1:]

# =============================================================================
# Splitting the dataset into the training set and test set
# =============================================================================
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# =============================================================================
# Multiple Linear Regression to the Training set
# =============================================================================
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# =============================================================================
# Predicting the Test set result
# =============================================================================
y_pred = regressor.predict(X_test)
regressor.score(X_test,y_pred)

# =============================================================================
# Building the otimal model using Backward Elimination
# =============================================================================
import statsmodels.formula.api as sm
X = np.append(arr= np.ones((50,1)).astype(int), values= X,axis=1)
X_opt = X[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()

X_opt = X[:,[0,1,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary() 

X_opt = X[:,[0,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary() 

X_opt = X[:,[0,3]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary() 
