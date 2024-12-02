from flask import Flask,render_template,request,jsonify
import pickle
import config
import json
import numpy as np
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Mysql1234"
app.config["MYSQL_DB"] = "BOSTON_DB"
mysql = MySQL(app)

with open(config.MODEL_PATH,"rb") as f:
    model = pickle.load(f)

with open(config.STD_SCALAR_PATH,"rb") as f:
    std_scalar = pickle.load(f)

with open(config.JSON_PATH,"r") as f:
    json_data = json.load(f) 


@app.route("/")
def home():   
    return render_template("index.html")


@app.route("/predict_price",methods = ["GET","POST"])
def predict():
    data = request.form 
    test_array = np.zeros(13) 

    test_array[0] = eval(data['CRIM'])
    a = test_array[0]
    test_array[1] = eval(data['ZN'])
    b = test_array[1]
    test_array[2] = eval(data['INDUS'])
    c = test_array[2]
    test_array[3] = eval(data['CHAS'])
    d = test_array[3]
    test_array[4] = eval(data['NOX'])
    e = test_array[4]
    test_array[5] = eval(data['RM'])
    f = test_array[5]
    test_array[6] = eval(data['AGE'])
    g = test_array[6]
    test_array[7] = eval(data['DIS'])
    h = test_array[7]
    test_array[8] = eval(data['RAD'])
    i = test_array[8]
    test_array[9] = eval(data['TAX'])
    j = test_array[9]
    test_array[10] = eval(data['PTRATIO'])
    k = test_array[10]
    test_array[11] = eval(data['B'])
    l = test_array[11]
    test_array[12] = eval(data['LSTAT'])
    m = test_array[12]
    std_array = std_scalar.transform([test_array])

    price_ = model.predict(std_array)

    price = np.round(price_[0],2)
    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS BOSTON(CRIM VARCHAR(20),ZN VARCHAR(20),INDUS VARCHAR(20),CHAS VARCHAR(20),NOX VARCHAR(20),RM VARCHAR(20),AGE VARCHAR(20),DIS VARCHAR(20),RAD VARCHAR(20),TAX VARCHAR(20),PTRATIO VARCHAR(20),B VARCHAR(20),LSTAT VARCHAR(20),PRICE VARCHAR(20))'
    cursor.execute(query)
    cursor.execute('INSERT INTO BOSTON(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,PRICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(a,b,c,d,e,f,g,h,i,j,k,l,m,price))

    mysql.connection.commit()
    cursor.close()

    return render_template("index1.html",price=price)

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)




 