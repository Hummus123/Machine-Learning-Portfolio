# -*- coding: utf-8 -*-
"""Copy of hw 3: knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCmDeHtyoJIAGRlguJNlCq3SF8sgoMU1

# Implementing a k-neareast neighbour class

Below you can find an incomplete implementaion of the kNN model as a class.
Complete the implementation based on the given instructions. Compare your result with sklearn library. 
Is your implementation faster or slower?
"""

import numpy as np

class KNNClassification():
    def __init__(self, k):
        """
        this is the constructor of the class. The constructor receives k (number of neighbours) and stores it.
        :param k: number of neighbours

        :return nothing
        
        """
        self.k = k# write your code here

        # later in `fit` function, we want to memorize our data and labels.
        # so in our constructor, we create some placeholder and then we will
        # populate these with real data. 
        self.X = None  
        self.y = None  

    def _compute_dist_one_pair(self, a, b):
        """
        this is a helper function to compute distance between two vectors `a` and `b`. 

        explanation: helper functions are functions that are used internally in a class. 
                     The common convection is to start the name of helper function with a _.
                     This means that users are not expected to use these functions.

        :param a, b: 1d numpy arrray of size m
        :return float
        
        """
        # write your code here (1 line)
        for i in range(len(b)):
            dist = (a[i] - b[i])**2
        return np.sqrt(dist)

    def compute_dist(self, new_x):
        """
        this function compute the distance of a new data `new_x` from all training data `self.X`.
        the output is a numpy array of size n, where n is the number of data in the training dataset.

        should only be used after `fit` is called. 
        should return a RunTimeError if `fit` is not called.

        :param new_x: 1d numpy arrray of size m
        :return numpy array of float
        
        """
        if self.X is None or self.y is None:
            raise RuntimeError("you should first call `fit` method.")

        # write your code here (~4-5 lines)
        lis = []
        for i in self.X:
            lis.append(self._compute_dist_one_pair(i, new_x))
        return np.array(lis)

    
    def fit(self, X, y):
        """
        for KNN, we only need to remember our training data (X) and labels (y)
        
        :param X: 2d numpy arrray of size n, m
        :param y: 1d numpy arrray of size n
        :return nothing
        
        """
        # write your code here (~2 lines)
        self.X = np.array(X)
        self.y = np.array(y)
    

    def predict(self, x_pred):
        """
        This function predicts the label of a new data instant `x_pred`.
        To do so, it computes the distance of the new data from 
        all data in our training dataset (using compute_dist function) and 
        find the k nearest neighbours. Then choose the most common label among the k neighbours.

        :param x_pred: 1d numpy arrray of size m
        :return predicted label

        """
        # write your code here (~5-10 lines)
        distances = self.compute_dist(x_pred)
        newlist = []
        for i in range(len(distances)):
            newlist.append((distances[i], y[i]))
        newlist.sort(key = lambda y : y[0])


        if sum(x[1] for x in newlist[:self.k]) > len(newlist[:self.k])/2:
            return 1
        else:
            return 0

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
# preprocessing, please do not change this part
cancer = load_breast_cancer()
columns = np.append(cancer.feature_names,['target'])
index = pd.RangeIndex(start=0, stop=len(cancer.data), step=1)
data = np.append(cancer.data, cancer.target[:,None], axis=1)
cancer_df = pd.DataFrame(data=data, index=index, columns=columns)

top_features = ["worst concave points", "worst perimeter", "mean concave points"]
X = cancer_df[top_features].to_numpy()
y = cancer_df["target"].to_numpy()

acc = []
k_list = range(1, 100, 2)
for i in k_list:
    test = KNNClassification(i+1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    g = []
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled  = scaler.transform(X_test)
    test.fit(X_train_scaled, y_train)
    for i in X_test_scaled:
        g.append(test.predict(i))
    acc.append((y_test == g).sum()/len(g))

import matplotlib.pyplot as plt
plt.figure(figsize= (10,6))
plt.plot(k_list, acc, 'ro--', linewidth=2)
plt.xlabel("k")
plt.ylabel("accuracy")
