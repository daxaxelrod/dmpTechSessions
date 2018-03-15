from flask import Flask
app = Flask(__name__)

@app.route("/")
def birthday():
    return "Happy birthday! Enjoy the skittles. <a href='/dmp'>clickable</a>           "

@app.route("/dmp")
def president():
    return "Gabe is the president.   <a href='/'>clickable</a>"
