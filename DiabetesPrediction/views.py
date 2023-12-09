from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from django.utils.datastructures import MultiValueDictKeyError

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(r'C:\Users\irfan\Documents\KULIAH\Semester 5\diabetes.csv')

    x = data.drop('Outcome', axis=1)
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    model = GaussianNB()
    model.fit(X_train, y_train)

    show_popup = False
    try:
        values = [float(request.GET.get(param, 0)) for param in ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8']]
        pred = model.predict([values])
        result1 = "Positive" if pred == [1] else "Negative"

        probabilities = model.predict_proba([values])
        probability_no_diabetes, probability_diabetes = probabilities[0]

        show_popup = True

    except MultiValueDictKeyError:
        result1 = probability_diabetes = probability_no_diabetes = None

    return render(request, "predict.html", {
        "result2": result1, 
        "resultno": probability_no_diabetes, 
        "resultyes": probability_diabetes,
        "show_popup": show_popup
    })