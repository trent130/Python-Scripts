#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets
dataset = pd.read_csv('Iris.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 5].values

#Taking missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean',)
imputer.fit(X[:, 1:4])
X[:, 1:4] = imputer.transform(X[:, 1:4])

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_y = LabelEncoder()
Y[:] = label_encoder_y.fit_transform(Y[:])
Y = Y.reshape(-1, 1)
onehotencoder = OneHotEncoder(sparse_output=True)
Y = onehotencoder.fit_transform(Y)

#splitting dataset in training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)