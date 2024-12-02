from flask import Flask,jsonify,render_template,request
from Project_Heart.utils import Heart
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

#this is for sql database connections
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] ="Mysql1234"
app.config["MYSQL_DB"] = "nileshdb"
mysql=MySQL(app)

@app.route("/")
def home():
    # return "we are in the flask now"
    return render_template ("Start.html")


@app.route("/medic",methods=["GET","POST"])
def get_prediction():
    data=request.form
    
    age=eval(data["age"])
    creatinine_phosphokinase=eval(data["creatinine_phosphokinase"])
    diabetes=eval(data["diabetes"])
    ejection_fraction=eval(data["ejection_fraction"])
    platelets=eval(data["platelets"])
    serum_creatinine=eval(data["serum_creatinine"])
    serum_sodium=eval(data["serum_sodium"])
    sex=eval(data["sex"])
    time=eval(data["time"])

    mlmodel=Heart(age,creatinine_phosphokinase,diabetes,ejection_fraction,platelets,serum_creatinine,serum_sodium,sex,time)
    r =mlmodel.get_medic()

    if r==1:
        result="The patient will enjoy his last days"
    else:
        result="The patient is totally healthy"
    
    

    cursor = mysql.connection.cursor()
    query = "create table if not exists heart(age varchar(10),creatinine_phosphokinase varchar(10),diabetes varchar(10),ejection_fraction varchar(10),platelets varchar(10),serum_creatinine varchar(10),serum_sodium varchar(10),sex varchar(10),time varchar(10),result varchar(50))"
    cursor.execute(query)
    cursor.execute("insert into heart (age,creatinine_phosphokinase,diabetes,ejection_fraction,platelets,serum_creatinine,serum_sodium,sex,time,result) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(age,creatinine_phosphokinase,diabetes,ejection_fraction,platelets,serum_creatinine,serum_sodium,sex,time,result))
    mysql.connection.commit()
    cursor.close()

    # return jsonify("prediction":{f"The result of the test : {result}"})
    return render_template ("End.html",result=result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.port_number)




