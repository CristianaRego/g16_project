from flask import Flask, render_template, request, session
from datafile import filename
from classes.devices import Devices
from classes.customer import Customer
from classes.plans import Plans
from classes.subscriptions import Subscriptions
from classes.userlogin import Userlogin
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin
import subs.subs_customerFoto as customerfsub
import os
from subs.apps_plot import apps_plot

app = Flask(__name__)

Devices.read(filename + 'G16.db')
Customer.read(filename + 'G16.db')
Plans.read(filename + 'G16.db')
Subscriptions.read(filename + 'G16.db')
Userlogin.read(filename + 'G16.db')
app.secret_key = 'BAD_SECRET_KEY'

upload_folder=os.path.join('static', 'fotos')
app.config['UPLOAD']=upload_folder


@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)

@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)

@app.route("/plot", methods=["post","get"])
def plot():
    return apps_plot()

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()

    
@app.route("/customer_foto", methods=["post","get"])
def subfoto():
    cname = 'Customer'
    return customerfsub.customerFotoform(app,cname)


if __name__ == '__main__':
    app.run(debug=True)
    
    