from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "kailas@4225",
    database = "student_raw1"
)
data = conn.cursor()

@app.route("/",methods=["GET","POST"])
def home():
     if request.method=="POST":
        name = request.form.get("name")
        age  = request.form.get("age")
        email = request.form.get("email")
        action = request.form.get("action")

        if action=="insert":

            check_email = "SELECT * FROM student WHERE email=%s"
            data.execute(check_email,(email,))
            result = data.fetchone()
            if result:
                return f"Already taken ! please try another email"


            if int(age)<=18:
                return f"Age must be greater than 18 "

            sql = "INSERT INTO student(name,age,email) VALUES(%s,%s,%s)"
            val = (name,age,email)
            data.execute(sql,val)
            conn.commit()
            return f"data saved"

        elif action=="update":
            sql = "UPDATE student SET email=%s WHERE name=%s"
            val = (email,name)
            data.execute(sql,val)
            conn.commit()
            return f"email updated"
     return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)