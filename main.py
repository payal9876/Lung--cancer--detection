import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle



data=pd.read_csv("lung_cancer_data.csv")

# feature engineering

df=pd.get_dummies(data,columns=['GENDER','LUNG_CANCER'],drop_first=True)
x=df.iloc[:,:-1]
y=df.iloc[:,-1]

# model_trainer
reg=LogisticRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
reg.fit(x_train,y_train)


# saving pickle object
filename='model.pkl'
pickle.dump(reg,open(filename,'wb'))
