from flask import Flask,render_template,request
app=Flask(__name__,template_folder="templates")
import numpy as np
import pyttsx3
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

import pickle
model=pickle.load(open("pomidor.pkl","rb"))
@app.route("/")
def fun():
    return render_template('pomidor.html')
@app.route("/predict",methods=["GET","POST"])
def func1():
    a= [int(i) for i in request.form.values()]
    print(a)
    a=np.array(a).reshape(1,-1)
    sol=model.predict(a)[0]
    return render_template("pomidor.html",value=sol)
if __name__=="__main__":
    app.run(debug=True)
