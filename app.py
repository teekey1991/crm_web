from flask import Flask, render_template, request, redirect, url_for
from config import Customer
app = Flask(__name__)


@app.route('/index')
def index():
    # customers = [
    #     Customer(name="Bob", age=79),
    #     Customer(name="Tom", age=57),
    #     Customer(name="Ken", age=73),
    # ]
    customers = Customer.select()
    return render_template("index.html", customers=customers)

@app.route("/add",methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]

    Customer.create(name=name, age=age) #インスタンスを作らずにセーブできる

    # return redirect("/index")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)