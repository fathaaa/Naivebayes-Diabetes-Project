from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(r'C:\Users\irfan\Documents\KULIAH\Semester 5\diabetes.csv')

    x = data.drop('Outcome', axis =1)
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    # X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

    model = GaussianNB()
    model.fit(X_train, y_train)
    try:
        val1 = float(request.GET['n1'])
        val2 = float(request.GET['n2'])
        val3 = float(request.GET['n3'])
        val4 = float(request.GET['n4'])
        val5 = float(request.GET['n5'])
        val6 = float(request.GET['n6'])
        val7 = float(request.GET['n7'])
        val8 = float(request.GET['n8'])
    
    except MultiValueDictKeyError:
        val1 = val2 = val3 = val4 = val5 = val6 = val7 = val8 = 0

    pred = model.predict([[val1, val2, val3,val4,val5,val6,val7,val8]])

    result1=""
    if pred ==[1]:
        result1="positive"
    else: 
        result1="negative"

    probabilities = model.predict_proba([[val1, val2, val3,val4,val5,val6,val7,val8]])
    probability_no_diabetes = probabilities[0, 0]
    probability_diabetes = probabilities[0, 1]

    return render(request, "predict.html", {"result2" : result1, "resultno" : probability_no_diabetes, "resultyes" : probability_diabetes} )