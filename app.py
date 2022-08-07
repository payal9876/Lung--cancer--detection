from flask import Flask,request,render_template


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])

def starting_model():
    return render_template("index.html")




    




if __name__=="main":
    app.run(debug=True)
