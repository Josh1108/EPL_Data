
import praw
import pandas as pd
import datetime as dt
import logging
import numpy as np
from numpy import random
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report


def logisticreg(X_train, X_test, y_train, y_test):
    from sklearn.linear_model import LogisticRegression

    logreg = Pipeline([('vect', CountVectorizer()),
                  ('tfidf', TfidfTransformer()),
                  ('clf', LogisticRegression(n_jobs=1, C=1e5)),
                 ])
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)

    print('accuracy %s' % accuracy_score(y_pred, y_test))
    print(classification_report(y_test, y_pred,target_names=flairs))

def train_test(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

    # print("Results of Naive Bayes Classifier")
    # nb_classifier(X_train, X_test, y_train, y_test)
    # print("Results of Linear Support Vector Machine")
    # linear_svm(X_train, X_test, y_train, y_test)
    print("Results of Logistic Regression")
    logisticreg(X_train, X_test, y_train, y_test)
    # print("Results of Random Forest")
    # randomforest(X_train, X_test, y_train, y_test)
    # print("Results of MLP Classifier")
    # mlpclassifier(X_train, X_test, y_train, y_test)

df =pd.read_csv('../Datasets/EPL_Set.csv')
print(df.head())
