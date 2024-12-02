from flask import Flask,render_template,jsonify,request
from project_data.utils import diabetics
import config
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] ="root123"
# app.config["MYSQL_DB"] = "demo1"
# mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")
    # return "We are in flask"


def Initiate():
    return 'Project Started'

@app.route('/pred',methods=['GET','POST'])
def get_predict():
    data = request.form

    
    Pregnancies           = eval(data['Pregnancies'])
    Glucose               = eval(data['Glucose'])
    BloodPressure         = eval(data['BloodPressure'])
    SkinThickness         = eval(data['SkinThickness'])
    Insulin               = eval(data['Insulin'])
    BMI                   = eval(data['BMI'])
    DiabetesPedigreeFunction     = eval(data['DiabetesPedigreeFunction'])
    Age                  = eval(data['Age'])

    dt_model = diabetics(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

    result   = dt_model.diabetics_prediction()

    # cursor = mysql.connection.cursor()
    # query = 'CREATE TABLE IF NOT EXISTS Diabetics(Pregnancies VARCHAR(30),Glucose VARCHAR(30),BloodPressure VARCHAR(30),SkinThickness VARCHAR(30), Insulin VARCHAR(30), BMI VARCHAR(30), DiabetesPedigreeFunction VARCHAR(30), Age VARCHAR(30),result VARCHAR(30))'
    # cursor.execute(query)
    # cursor.execute('INSERT INTO Diabetics(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,result)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,result))

    # mysql.connection.commit()
    # cursor.close()
    return render_template("index1.html",result=result)

    # return jsonify({'prediction':f"The elisibility of a customer :{result}"})



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)
