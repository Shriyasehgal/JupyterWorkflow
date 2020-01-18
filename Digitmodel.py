import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn import ensemble
import pickle

digits= pd.read_csv("DigitRec/csv/newtraindataset.csv")

digits.rename(columns={'0':'Label'})

x=digits.iloc[:,1:]
y=digits.iloc[:,0]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)
classifier = ensemble.RandomForestClassifier()

classifier.fit(x_train, y_train)

pickle.dump(classifier,open("DigitRec/model/Model","wb"))

score=classifier.score(x_test,y_test)
print(score)
