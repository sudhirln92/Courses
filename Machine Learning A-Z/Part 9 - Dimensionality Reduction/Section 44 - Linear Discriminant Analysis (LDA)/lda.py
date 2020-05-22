#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:45:47 2018

@author: sudhir
"""
# =============================================================================
# Import library
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
#  Importing data
# =============================================================================
dataset=pd.read_csv('Wine.csv')
X=dataset.iloc[:, 0:13].values
y=dataset.iloc[:,13].values
#y = dataset.loc[:,'Purchased'].values # Dependent variable
dataset.head()
dataset.tail()

# =============================================================================
# Splitting the dataset into the training set and test set
# =============================================================================
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# =============================================================================
# Feature scaling
# =============================================================================
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# =============================================================================
# Applying LDA
# =============================================================================
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=2)

X_train = lda.fit_transform(X_train,y_train)
X_test = lda.transform(X_test)

# =============================================================================
# Fitting Logistic Regression to the training set
# =============================================================================
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state= 0,)
classifier.fit(X_train, y_train)

# =============================================================================
# Predicting the Test result
# =============================================================================
y_pred = classifier.predict(X_test)

# =============================================================================
# Making Confusion Matrix
# =============================================================================
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# =============================================================================
# Visualize training and testing set result
# =============================================================================
from matplotlib.colors import ListedColormap

def plot_decision_boundary(X_set,y_set,classifier,dataset):
    X1,X2 = np.meshgrid(np.arange(X_set[:,0].min()-1,X_set[:,0].max()+1, step=0.01),
                        np.arange(X_set[:,1].min()-1,X_set[:,1].max()+1, step=0.01))
    X_new = np.c_[X1.ravel(),X2.ravel()]
    pred = classifier.predict(X_new).reshape(X1.shape)
    plt.contourf(X1,X2,pred, alpha=0.2, cmap=ListedColormap(('red','green','blue')))
    
    plt.scatter(X_set[:,0][y_set==1], X_set[:,1][y_set==1], c='r', s=10, label='1')
    plt.scatter(X_set[:,0][y_set==2], X_set[:,1][y_set==2], c='g', s=10,label='2')
    plt.scatter(X_set[:,0][y_set==3], X_set[:,1][y_set==3], c='b', s=10,label='3')
    plt.xlim(X1.min(),X1.max())
    plt.ylim(X2.min(),X2.max())
    plt.title('Logistic Regression'+dataset)
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.legend()
    plt.show()
    
plot_decision_boundary(X_train,y_train,classifier,' Training set')

plot_decision_boundary(X_test,y_test,classifier,' Testing set')
