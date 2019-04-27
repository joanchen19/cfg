from flask import Flask, render_template, request
from send_msg import send_simple_message
from generate_bouquet import bouquet_generator

app = Flask("MyApp")

@app.route("/")
def main():
    return render_template("landingpage.html")

@app.route("/bouquets")
def bouquets():
    return render_template("bouquets.html")

@app.route("/order", methods=["POST"])
def generate_order(bouquet=None):
    form_data = request.form
    bouquet = bouquet_generator(form_data)
    print form_data
    return render_template("bouquets_result.html", bouquet=bouquet)

@app.route("/submitted-order", methods=["POST"])
def sign_up():
    form_data = request.form
    print "Name: " + form_data["first-name"] + " " + form_data["last-name"]
    print "Email: " + form_data["email"]
    send_simple_message(form_data["email"])
    return "Email sent to " + form_data["email"] + ", please check your inbox."


app.run(debug=True)
