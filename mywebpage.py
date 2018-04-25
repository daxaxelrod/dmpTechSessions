from flask import Flask, render_template, request
import sendgrid
import os
from sendgrid.helpers.mail import *
from datetime import datetime


app = Flask(__name__)

# email handling
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))


def send_email_to_self(name, email, message):
    from_email = Email("hello@abigail.com")
    to_email = Email("agiambr3@binghamton.edu")
    subject = name + " wants to connect with you"
    today = datetime.today()
    email_content = Content("text/plain", "{} contacted you on {} \n Their email is {} and their message is below \n {}"
                    .format(name, today, email, message))
    print("sending an email to me from {}".format(name))
    mail = Mail(from_email, subject, to_email, email_content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)

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
