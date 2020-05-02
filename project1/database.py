import os

from flask import Flask, session,request,render_template,redirect
from flask_session import Session
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import scoped_session, sessionmaker
from Tables import *
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# Session = scoped_session(sessionmaker(bind=engine))
# session = Session()


@app.route("/")
def index():
    return redirect("/Register")


@app.route("/Register", methods = ['POST', 'GET'])
def Output():
    db.create_all()
    if request.method =='POST':
        userdata = Tables(request.form["Username"],request.form["psw"])
        users = Tables.query.filter_by(Username=request.form["Username"]).first()
        if users is not None:
            message = "User name is already existing.Register with new user name"
            return render_template("Registration.html",message1 = message)
        db.session.add(userdata)
        db.session.commit()
        message = "Registartion is successful"
        return render_template("Registration.html",message = message)
    #     result = request.form
    #     print(result['Username'])
    else:
        return render_template("Registration.html")
@app.route('/admin')
def admin():
    allusersdata = Tables.query.order_by(desc(Tables.timestamp)).all()
    return render_template("administration.html",admin = allusersdata)

@app.route("/auth",methods = ["POST"])
def login():
    users = Tables.query.filter_by(Username=request.form["Username"]).first()
    if users is not None:
        if request.form["psw"]==users.psw:
            session["Username"] = request.form["Username"]
            return redirect("/homepage")
        else:
            message = "Wrong credentials"
            return render_template("Registration.html", message = message)
    else:
        message = "You are not registered user but trying to login"
        return render_template("Registration.html",message = message)
@app.route("/homepage")
def homepage():
    try:
        users = session["Username"]
        return render_template("login.html")
    except:
        message = "login to view the homepage"
        return render_template("Registration.html",message = message)
@app.route("/logout")
def logout():
    try:
        session.clear()
        message = "Logged out Successful"
        return render_template("Registration.html",message = message)
    except:
        message = "You have to login to logout"
        return render_template("Registration.html",message = message)