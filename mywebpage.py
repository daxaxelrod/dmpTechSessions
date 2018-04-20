from flask import Flask, render_template, request
app = Flask(__name__)

def send_email_to_self(name, email, message):
    print("sending an email to me from {}".format(name))

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        name = request.form["first_name"]
        email = request.form["email"]
        message = request.form["message"]
        send_email_to_self(name, email, message)
        return render_template("index.html", email_sent = "Thank you!")
    return render_template("index.html")
