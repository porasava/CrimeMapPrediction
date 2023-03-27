import numpy as np
import streamlit as st
import pickle
import pandas as pd
from sklearn.neighbors import  KNeighborsClassifier

from datetime import datetime
import pandas as pd
from geoCrimeapp.models import Crime_data, Crime_prediction
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import time
import csv
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report
process_time = []

    # Add Crime data from 2017-2022
df_train=pd.read_csv(r"data\NewTable08_Map_Crime_MY50714imblearn_Year1to5_Area.csv")
    # df2=pd.read_csv(r"C:\Users\admin\Downloads\Sample_crime_1000recordsMY5.xlsx")
df_test=pd.read_csv(r"data\NewTable08_Map_Crime_MY50714imblearn_Year6_M1_F100_Area.csv")

X = df_train[['Month',
            'Day_Of_Week_ID', 'HRGroup','Area_unitID', 'TA_ID',
           'Locn_Type_DivisionID','Types_of_Crime_ID']]
y =df_train[['Number_of_records']]
X_new = df_test[['Month'
           , 'Day_Of_Week_ID', 'HRGroup', 'Area_unitID','TA_ID',
           'Locn_Type_DivisionID','Types_of_Crime_ID']]
y_new =df_test[['Number_of_records']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=50)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
knn_score=knn.score(X_test,y_test)

pickle.dump(knn,open('Crime_KNN.pkl',"wb"))


