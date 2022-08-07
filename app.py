from flask import Flask,request,render_template


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])

def starting_model():
    return "THIS IS JUST STARTING"




    




if __name__=="main":
    app.run(debug=True)
