from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/Register")
def Register():
    return render_template("Registration.html")

if __name__ == '__main__':
    app.run(debug = True)