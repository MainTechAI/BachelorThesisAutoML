# -*- coding: utf-8 -*-
"""
API test
"""
from auto import ModelSelection
import pandas as pd

used_algo = {
    'AdaBoost': True,
    'XGBoost': True,
    'Bagging(SVC)': True,
    'MLP': True,
    'HistGB': True,
    'Ridge': False,
    'LinearSVC': True,
    'PassiveAggressive': False,
    'LogisticRegression': False,
    'LDA': False,
    'QDA': False,
    'Perceptron': False,
    'SVM': True,
    'RandomForest': True,
    'xRandTrees': True,
    'ELM': False,
    'DecisionTree': False,
    'SGD': False,
    'KNeighbors': True,
    'NearestCentroid': False,
    'GaussianProcess': False,
    'LabelSpreading': True,
    'BernoulliNB': False,
    'GaussianNB': False,
    'DBN': False,
    'FactorizationMachine': False,
    'PolynomialNetwork': False,
}

MS = ModelSelection(
    experiment_name='experiment_api_test',
    duration=40,
    min_accuracy=65.0,
    max_model_memory=10485760,
    max_prediction_time=400,
    max_train_time=30,
    used_algorithms=used_algo,
    metric='accuracy',
    validation='10 fold CV',
    saved_models_count='All',
    iterations=40,
)

# three ways to specify a path string
# DS_path=r'C:\Users\dosto\.+DATASETS\breast-w\breast-w.csv'
# DS_path='C:/Users/dosto/.+DATASETS/breast-w/breast-w.csv'
DS_path = 'C:\\Users\\dosto\\.+DATASETS\\breast-w\\breast-w.csv'

DS = pd.read_csv(DS_path, skiprows=0).values

MS.fit(
    x=DS,
    y=DS[:, 9],
    num_features=[0,1,2,3,4,5,6,7,8],
    #cat_features=cat_cols,
    #txt_features=txt_cols,
)

MS.save_n_best_on_disk()

