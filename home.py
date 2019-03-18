from flask import Flask, render_template, request
from send_msg import send_simple_message

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
    return render_template("home.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print "Name: " + form_data["first-name"] + " " + form_data["last-name"]
    print "Email: " + form_data["email"]
    print "Gender: " + form_data["gender"]
    send_simple_message(form_data["email"])
    return "Email sent to " + form_data["email"] + ", please check your inbox."


app.run(debug=True)
