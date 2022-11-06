from flask import Flask,request,render_template
import pickle

app = Flask(__name__)



@app.route("/") 
def about():
    return render_template("home.html")

@app.route("/home") 
def home():
    return render_template("home.html")

@app.route("/upload")
def test():
    return render_template("pred.html")


if __name__ == '__main__':
    app.run()