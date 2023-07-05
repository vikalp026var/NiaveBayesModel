from flask import Flask,app,render_template,request
from flask import Response
import pymongo
import numpy 
import pickle

app=Flask(__name__)
uri=("mongodb+srv://vikalp026varshney:vikalp026var@cluster0.r31hq0n.mongodb.net/?retryWrites=true&w=majority")
client=pymongo.MongoClient(uri)
db=client['Naive_Bayes']
collection=db["collections"]
scale=pickle.load(open('scalenaive.pkl','rb'))
model=pickle.load(open('naivebayes.pkl','rb'))
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/data',methods=['GET','POST'])
def naive():
    if request.method=='POST':
        sepal_length=float(request.form.get("sepal_length"))
        sepal_width=float(request.form.get("sepal_width"))
        petal_length=float(request.form.get("petal_length"))
        petal_width=float(request.form.get("petal_width"))
        new_data=scale.transform([[sepal_length,sepal_width,petal_length, petal_width]])
        result=model.predict(new_data)[0]
        collection.insert_many([{'Sepal_length':sepal_length,'Sepal_width':sepal_width,'Petal_length':petal_length,'Petal_width':petal_width,'Species':result}])
    return render_template('home.html',result=result)
if __name__=="__main__":
    app.run(host="0.0.0.0")


        
        