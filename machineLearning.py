import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from pprint import pprint

data = pd.read_csv("creditcardcsvpresent.csv")
data = data.drop("6-month_chbk_freq", axis=1)
data = data.drop("Transaction date", axis=1) #Data table without null values
data = data.drop("6_month_avg_chbk_amt", axis = 1)
data = data.drop("Daily_chargeback_avg_amt", axis = 1)
data = data.drop("Merchant_id", axis=1)
#data = data.drop("Is declined", axis = 1)
data=data.drop("Total Number of declines/day", axis = 1)

def mybool(value):
    if value=="Y":
        return 1
    elif value=="N":
        return 0

#data["Is declined"] = [mybool(x) for x in data["Is declined"]]
#Applies function to every item x in column and reassign values to column
data["isForeignTransaction"] = [mybool(x) for x in data["isForeignTransaction"]]
data["isHighRiskCountry"] = [mybool(x) for x in data["isHighRiskCountry"]]
data["isFradulent"] = [mybool(x) for x in data["isFradulent"]]
data["Is declined"] = [mybool(x) for x in data["Is declined"]]
data.sample(3)
#data = data.drop("Is declined", axis = 1)

target=data["isFradulent"]

predictors=data.drop("isFradulent", axis=1)

X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.2)



def predictKNN(x, name, text):
    # KNN or k-Nearest Neighbors
    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    y_pred = knn.predict(x)
    print("\t\t** results for {} (KNN)**".format(name))
    print("\t\t{}".format(text))
    if (y_pred[0] == 1):
        print("\nYes, this is likely to be fraudulent\n")
    else:
        print("\nNo, this is not likely to be fraudulent\n")

def predict(x, name, text):
    decisiontree = DecisionTreeClassifier()
    decisiontree.fit(X_train, y_train)
    from sklearn.metrics import accuracy_score

    y_pred = decisiontree.predict(x)
    #acc_decisiontree = round(accuracy_score(y_pred, y_test) * 100, 2)
    #print(acc_decisiontree)
    print("\t\t** results for {} (Decision Tree)**".format(name))
    print("\t\t{}".format(text))
    if (y_pred[0] == 1):
        print("Yes, this is likely to be fraudulent\n")
    else:
        print("No, this is not likely to be fraudulent\n")

#predict(X_test)




