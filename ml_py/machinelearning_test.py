# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:44:00 2019

Trying out sklearn for machine learning following this guide:
https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn#step-1

@author: Micaela
"""
# import libraries and modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Cross-validation pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# Evaluation Metrics
from sklearn.metrics import mean_squared_error, r2_score

# Module for saving scikit-learn models
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


# 3. Load in Data 
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

print(data.head(5))

print(data.shape)

print(data.describe())

## data are all numeric, but ranges differ between data. 
## STANDARDIZE vars?

# 4. Split Data in Training and Test Set
y = data.quality # target
X = data.drop('quality', axis=1) # input feature X

# Use train_test_split function from sklearn
# both the input and target has to be separated into sets
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123, 
                                                    stratify=y)
## Step 5: Declare data preprocessing steps.
# a. standardized columns (mean=0, sd = 1)
# b . check standardization
# c. Make pipeline for standardization + randomforest
X_train_scaled = preprocessing.scale(X_train)
print(X_train_scaled)
X_train_scaled.std(axis=0)
X_train_scaled.std(axis=0)
print(X_train_scaled.mean(axis=1))
	
scaler = preprocessing.StandardScaler().fit(X_train)

print(scaler.fit)


pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))

## Step 6: Declare hyperparameters to tune.
print(pipeline.get_params())

# declare the hyperparameters we want to tune through cross-validation.
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}

## Step 7: Tune model using a cross-validation pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)

# Fit and tune model
clf.fit(X_train, y_train)

print(clf.best_params_)
# OUTPUT of best_params_ 
#{'randomforestregressor__max_depth': None, '
# randomforestregressor__max_features': 'log2'}

# Step 8:refit enbtire training set
# GridSearchCV  autamatically refits the model ln77
print(clf.refit) # confirm model will be retrained

# Step 9: Evaluate model pipeline on test data.
# Predict a new set of data
y_pred = clf.predict(X_test)


r2_score(y_test, y_pred)

mean_squared_error(y_test, y_pred)


# Step 10. Save model f or future use
#save model as .pkl file
joblib.dump(clf, 'rf_regressor.pkl')


#Load model again
clf_old = joblib.load('rf_regressor.pkl')
clf_old.predict(X_test)

""" 
Is the model good enought?
1. Start with the goal of the model. If the model is tied to a business 
    problem, have you successfully solved the problem?
2. Look in academic literature to get a sense of the current performance 
    benchmarks for specific types of data.
3. Try to find low-hanging fruit in terms of ways to improve your model.

Ideas:
    Try other regression families, more data, engineer/generate better features, 
    spend more time on exploratory analysis to make better features

"""

