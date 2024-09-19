# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:02:57 2024

@author: Admin
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets
dataset = pd.read_csv('Salary.csv')

experience = dataset.iloc[:, 4].values.reshape(-1, 1)
salary = dataset.iloc[:, 5].values

# Handling missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
experience = imputer.fit_transform(experience)

#splitting dataset into training set and test set
from sklearn.model_selection import train_test_split
experience_train, experience_test, salary_train, salary_test = train_test_split(experience, salary, test_size=0.3, random_state=0)

#fitting a simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(experience_train, salary_train)

# Predicting the test set results
salary_pred = regressor.predict(experience_test)

# Visualizing the training set results
plt.scatter(experience_train, salary_train, color='red')
plt.plot(experience_train, regressor.predict(experience_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the test set results
plt.scatter(experience_test, salary_test, color='red')
plt.plot(experience_train, regressor.predict(experience_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
