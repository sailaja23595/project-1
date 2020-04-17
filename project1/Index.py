from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/Register", methods = ['POST', 'GET'])
def Output():
    if request.method =='POST':
        result = request.form
        return render_template("Output.html",Output = result)
    else:
        return render_template("Registration.html")
if __name__ == '__main__':
    app.run(debug = True)