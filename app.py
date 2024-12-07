from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route("/",methods=["GET"])
def homepage():
    return "Hi:)"

@app.route("/home",methods=["GET"])
def frontend():
    return render_template("index.html")

database=[]
@app.route("/reg_data",methods=["POST"])
def get_reg_data():
    user={}
    name=request.form["U_name"]
    phone=request.form["num"]
    email=request.form["U_mail"]
    password=request.form["U_pwd"]

    user["user_name"]=name
    user["user_phone"]=phone
    user["user_mail"]=email
    user["user_password"]=password
    database.append(user)
    return redirect("/home")

@app.route("/log_data",methods=["POST"])
def get_login_data():
    l_email=request.form["U_mail"]
    l_password=request.form["U_pwd"]
    for user in range(len(database)):
        email=database[user]["user_mail"]
        password=database[user]["user_password"]
        if email==l_email and password==l_password:
            return "login Successful"
    else:
        return "Invalid Credentials"
    return databases
app.run(debug=True)
