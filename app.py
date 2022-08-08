
from flask import Flask,request,render_template
import pickle
import pandas as pd
import numpy as np

model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])

def starting_model():
    return render_template("index.html")

def predict():

    AGE=int(request.form['AGE'])
    GENDER=(request.form['GENDER'])
    if (GENDER=='MALE'):
        GENDER=1
    else:
        GENDER=0

    SMOKING=(request.form['SMOKING'])
    if (SMOKING=='YES'):
        SMOKING=1
    else:
        SMOKING=2

    YELLOW_FINGERS=(request.form['YELLOW_FINGERS'])  
    if (YELLOW_FINGERS=='YES'):
       YELLOW_FINGERS=1
    else:
        SMOKING=2


    ANXIETY=(request.form['ANXIETY'])
    if(ANXIETY=='YES'):
        ANXIETY=1
    else:
        ANXIETY=2


    PEER_PRESSURE=(request.form['PEER_PRESSURE'])
    if (PEER_PRESSURE=='YES'):
        PEER_PRESSURE=1
    else:
        PEER_PRESSURE=2

    FATIGUE=(request.form['FATIGUE'])  
    if (FATIGUE=='YES'):
       FATIGUE=1
    else:
        FATIGUE=2


    CHRONIC_DISEASE=(request.form['CHRONIC_DISEASE'])
    if(CHRONIC_DISEASE=='YES'):
        CHRONIC_DISEASE=1
    else:
        CHRONIC_DISEASE=2

   

    ALLERGY=(request.form['ALLERGY'])  
    if (ALLERGY=='YES'):
       ALLERGY=1
    else:
        ALLERGY=2


    WHEEZING=(request.form['WHEEZING'])
    if(WHEEZING=='YES'):
        WHEEZING=1
    else:
        WHEEZING=2


    ALCOHOLCONSUMING=(request.form['ALCOHOLCONSUMING'])
    if (ALCOHOLCONSUMING=='YES'):
        ALCOHOLCONSUMING=1
    else:
        ALCOHOLCONSUMING=2

    COUGHING=(request.form['COUGHING'])  
    if (COUGHING=='YES'):
       COUGHING=1
    else:
        COUGHING=2


    SHORTNESSOFBREATH=(request.form['SHORTNESSOFBREATH'])
    if(SHORTNESSOFBREATH=='YES'):
        SHORTNESSOFBREATH=1
    else:
        SHORTNESSOFBREATH=2

    SWALLOWINGDIFFICULTY=(request.form['SWALLOWINGDIFFICULTY'])  
    if (SWALLOWINGDIFFICULTY=='YES'):
       SWALLOWINGDIFFICULTY=1
    else:
        SWALLOWINGDIFFICULTY=2


    CHESTPAIN=(request.form['CHESTPAIN'])
    if(CHESTPAIN=='YES'):
        CHESTPAIN=1
    else:
        CHESTPAIN=2

    data=['AGE','GENDER','SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','FATIGUE','CHRONIC_DISEASE','ALLERGY','WHEEZING','ALCOHOLCONSUMING','COUGHING','SHORTNESSOFBREATH','SWALLOWINGDIFFICULTY','CHESTPAIN']    
    features_value=[np.array(data)]

    feature_name=['AGE','GENDER','SMOKING','YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','FATIGUE','CHRONIC_DISEASE','ALLERGY','WHEEZING','ALCOHOLCONSUMING','COUGHING','SHORTNESSOFBREATH','SWALLOWINGDIFFICULTY','CHESTPAIN']    

    df=pd.DataFrame(features_value,columns=feature_name)
    mypred=model.predict(df)

    if mypred==1:
       mypred='yes'
    else:
       mypred='no'
    
    return render_template('result.html',prediction=mypred) 




if __name__=="main":
    app.run(debug=True)
