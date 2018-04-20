from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def birthday():
    # page = {}
    if request.method == "POST":
        print("analyzing user data")
        print(request.form)
        # return request.form["namebox"]
        our_user = request.form["namebox"]
        our_user = our_user.upper()*50

        first_number = int(request.form["number_1"])
        second_number = int(request.form["number_2"])

        answer = first_number + second_number
        print(answer)
        return render_template("homepage.html", my_answer = answer,
                                                username = our_user)
    #
    # add = 2+2
    # page["answer"] = add
    # page["username"] = "abigail"
    # print(page)

    return render_template("homepage.html",)
    # render_template(template_name_or_list, context)

@app.route("/dmp")
def president():
    return "Gabe is the president.   <a href='/'>clickable</a>"
