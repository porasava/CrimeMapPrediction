# from django.contrib import admin
# from datetime import datetime
# import pandas as pd
# from geoCrimeapp.models import Crime_data, Crime_prediction
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
# from sklearn.model_selection import GridSearchCV
# import time
# import csv
# from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report
# process_time = []


# # Register your models here.
# admin.site.register(Crime_data)
# admin.site.register(Crime_prediction)
# # if Crime_data.objects.all().count()==0:
#     # Add Crime data from 2017-2022
#     # df=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn.csv")
# #     # df2=pd.read_csv(r"C:\Users\admin\Downloads\Sample_crime_1000recordsMY5.xlsx")
# #     df=pd.read_csv(r"C:\Users\admin\Downloads\Sample_crime_1000recordsMY5.xlsx")
# # # #Preview df
# # df= pd.read_sql_table(Crime_data)
# # print(df.head())
# # print(df.head())
# # # df_load=df.drop(['new_column'],axis=1)
# # #print(df_load.head())

# # #rename column 
# # # df_load_re= df_load.rename(columns={'F1':'Territorial_Authority'})

# # # df_train_MY50714_drop=df_train_MY50714.dropna()

# # for index, row in df.iterrows():
# #     Month=row['Month']
# #     Year=row['Year']
# #     SHAPE_X=row['SHAPE_X']
# #     SHAPE_Y=row['SHAPE_Y']
# #     LATITUDE=row['LATITUDE']
# #     LONGITUDE=row['LONGITUDE']
# #     Area_unitID=row['Area_unitID']
# #     Day_Of_Week_ID=row['Day_Of_Week_ID']
# #     HRGroup=row['HRGroup']
# #     TA_ID=row['TA_ID']
# #     Locn_Type_DivisionID=row['Locn_Type_DivisionID']
# #     Types_of_Crime_ID=row['Types_of_Crime_ID']
# #     new_column=row['new_column']
# #     Number_of_records=row['Number_of_records']
   
    
# # Crime_data(
# # Month=Month,
# # Year=Year,
# # SHAPE_X=SHAPE_X,
# # SHAPE_Y=SHAPE_Y, 
# # LATITUDE=LATITUDE,
# # LONGITUDE=LONGITUDE,
# # Area_unitID=Area_unitID,
# # Day_Of_Week_ID=Day_Of_Week_ID, 
# # HRGroup=HRGroup,
# # TA_ID=TA_ID,
# # Locn_Type_DivisionID=Locn_Type_DivisionID,
# # Types_of_Crime_ID=Types_of_Crime_ID,
# # new_column=new_column,
# # Number_of_records=Number_of_records).save()

# if Crime_prediction.objects.all().count()==0:
#     df_train=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year1to5.csv")
#     df_test=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year6_M1_F100.csv")
#    # add test data 
#     # df_test=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year6_M1_F100.csv")

# df_train=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year1to5.csv")
# #     # pd.read_csv('ml-100k/u.item', sep='|', names=m_cols , encoding='latin-1')
# df_test=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year6_M1_F100.csv")
# # # df_train_load=df_train.drop([],axis=1)
# # # df_test_load=df_test.drop([],axis=1)
# #     df_test=pd.read_csv(r"C:\Users\admin\Downloads\NewTable08_Map_Crime_MY50714imblearn_Year6_M1_F100.csv")
#  # Assign classifier
# # Use default criterion (gini)
# # cls_rf = RandomForestClassifier(random_state=1, n_jobs=-1, n_estimators=90)
# # Split train and test set 90/10
# X = df_train[['Month', 'Year', 'SHAPE_X', 'SHAPE_Y', 'LATITUDE', 'LONGITUDE',
#             'Day_Of_Week_ID', 'HRGroup','Area_unitID', 'TA_ID',
#            'Locn_Type_DivisionID','Types_of_Crime_ID']]
# y =df_train[['Number_of_records']]
# X_new = df_test[['Month', 'Year', 'SHAPE_X', 'SHAPE_Y', 'LATITUDE', 'LONGITUDE'
#            , 'Day_Of_Week_ID', 'HRGroup', 'Area_unitID','TA_ID',
#            'Locn_Type_DivisionID','Types_of_Crime_ID']]
# y_new =df_test[['Number_of_records']]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=50)
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

# # #Build the model
# cls_rf = RandomForestClassifier(random_state=1, n_jobs=-1, n_estimators=90)
# cls_rf.fit(X_train, y_train.values.ravel())
# result=cls_rf.predict(X_test)
# score=cls_rf.score(X_test,y_test)*100
# print('Accuracy1: ', cls_rf.score(X_test, y_test))

# # # Fit model and run on test set with timing
# start_time = time.time()
# # Timing
# elapsed_time = time.time() - start_time
# print('Formatted time: ', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
# print('Time in seconds: ', elapsed_time)
# process_time.append(elapsed_time)

# # F1 score test
# pred = cls_rf.predict(X_test)
# print('F1 accuracy1: ', f1_score(pred, y_test, average='macro'))
#     # rfc_pred = rfc.predict(X_test)
# print (classification_report(y_test,pred))

# F1=f1_score(pred, y_test, average='macro')
# F1

# #predict X_new -> data year 2022 month 1-4
# final_result=cls_rf.predict(X_new)
# final_score=cls_rf.score(X_new, y_new)
# F1_X_new=f1_score(final_result,  y_new, average='macro')
# print('F1 accuracy2: ', F1_X_new)

#  # print result to list
# lst_Crime_Case =[]
# i=0
# for r in final_result.tolist():
#     lst_Crime_Case.append(final_result[i])
#     i += 1
#     df_results=X_new[[
#            'Month', 
#            'Year',
#             'LATITUDE', 'LONGITUDE',
#            'Area_unitID', 'TA_ID',
#             'Day_Of_Week_ID', 'HRGroup',
#            'Locn_Type_DivisionID', 
#             'Types_of_Crime_ID']]

#     df_results['Crime_Case'] = pd.Series(lst_Crime_Case)
#     df_results['Accuracy']=final_score
#     df_results['F1']=F1_X_new

#     #Preview the prediction
#     # print(df_results.head())

# #save to table
#     for index, row in df_results.iterrows():
#         Month=row['Month']
#         Year=row['Year']
#         LATITUDE=row['LATITUDE']
#         LONGITUDE=row['LONGITUDE']
#         Area_unitID=row['Area_unitID']
#         TA_ID=row['TA_ID']
#         Day_Of_Week_ID=row['Day_Of_Week_ID']
#         HRGroup=row['HRGroup']
#         Locn_Type_DivisionID=row['Locn_Type_DivisionID']
#         Types_of_Crime_ID=row['Types_of_Crime_ID']
#         Crime_Case=row['Crime_Case']
#         Accuracy=row['Accuracy']

#     Crime_prediction(Month=Month, Year=Year,LATITUDE=LATITUDE, LONGITUDE=LONGITUDE, Area_unitID=Area_unitID,
#     TA_ID=TA_ID, Day_Of_Week_ID=Day_Of_Week_ID, HRGroup=HRGroup, Locn_Type_DivisionID=Locn_Type_DivisionID,
#     Types_of_Crime_ID=Types_of_Crime_ID, Crime_Case=Crime_Case,
#     Accuracy=Accuracy).save()
