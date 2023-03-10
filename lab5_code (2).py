# -*- coding: utf-8 -*-
"""lab5_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mn5rvh4SnWfjyFXFDK8Mi1HCRoAcGeIB
"""

#---------LAB 5--------------

# tests to show that changing the training set would change the precision and the recall of the classifier





#---TEST 1, Using iris dataset


# load the iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
  
# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target
  
# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
  
# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
  
# making predictions on the testing set
y_pred = gnb.predict(X_test)
  
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

#---TEST 2, Using Wine Quality Dataset

# load the Wine Quality Dataset 
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.style.use("ggplot")

from sklearn import naive_bayes
  
# store the feature matrix (X) and response vector (y)
dataset = datasets.load_wine()
X = dataset.data 
y = dataset.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
  
# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
  
# making predictions on the testing set
y_pred = gnb.predict(X_test)
  
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

#---TEST 3, Using Pima Indians Diabetes Dataset

# load the Pima Indians Diabetes Dataset
import pandas as pd
data = pd.read_csv("diabetes.csv")

from sklearn.model_selection import train_test_split
  
# store the feature matrix (X) and response vector (y)
x = data.drop("Outcome", axis= 1)
y = data[["Outcome" ]]


# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( x,y,test_size=0.30, random_state=1)
  
# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
  
# making predictions on the testing set
y_pred = gnb.predict(X_test)
  
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)