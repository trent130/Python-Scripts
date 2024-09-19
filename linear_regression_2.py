# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:02:25 2024

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#loading the dataset
dataset = pd.read_csv('iris.csv')

#working on the dataset
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values

#splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,  random_state=0)

#