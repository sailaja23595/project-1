import os

from flask import Flask, session,request,render_template,redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Tables import *

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
Session = scoped_session(sessionmaker(bind=engine))
session = Session()


@app.route("/")
def index():
    return "Project 1: TODO"


@app.route("/Register", methods = ['POST', 'GET'])
def Output():
    db.create_all()
    if request.method =='POST':
        userdata = Tables(request.form["Username"],request.form["psw"])
        db.session.add(userdata)
        db.session.commit()
    #     result = request.form
    #     print(result['Username'])

        return render_template("Registration.html")
    else:
        return render_template("Registration.html")

