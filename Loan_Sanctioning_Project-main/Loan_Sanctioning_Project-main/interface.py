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
app.config["MYSQL_DB"] = "nileshdb"
mysql = MySQL(app)

with open(config.MODEL_PATH,"rb") as f:
    model = pickle.load(f)

with open(config.JSON_PATH,"r") as f:
    json_data = json.load(f) 


@app.route("/")
def home():   
    return render_template("Start.html")


@app.route("/predict_loan",methods = ["GET","POST"])
def predict():
    data = request.form 
    test_array = np.zeros(3) 

    test_array[0] = eval(data['LoanAmount'])
    a = test_array[0]
    test_array[1] = eval(data['Credit_History'])
    b = test_array[1]
    test_array[2] = eval(data['Property_Area'])
    c = test_array[2]

    decision = model.predict([test_array])

    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS Loan(LoanAmount VARCHAR(20),Credit_History VARCHAR(20),Property_Area VARCHAR(20),decision VARCHAR(20))'
    cursor.execute(query)
    cursor.execute('INSERT INTO Loan(LoanAmount,Credit_History,Property_Area,decision) VALUES(%s,%s,%s,%s)',(a,b,c,decision))

    mysql.connection.commit()
    cursor.close()

    return render_template("End.html",decision=decision)

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)




 