#Multiple linear regression

#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

#Spliting dataset into 
from sklearn.cross_validation import train_test_split
X_train,X_test, y_train, y_test=train_test_split(X,y,test_size=.2, random_state=0)


#Fitting the Decision Tree 
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,y)

#Predicting the test set result
y_pred = regressor.predict(6.5)

#Visualising the Decision Tree Regression result
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Truth or Bluff (Decision Tree regressor)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
