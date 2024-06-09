from os import getenv
from flask import Flask, render_template
from form import FormLogin
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5

from utils import handle_login

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("WTF_CSRF_SECRET_KEY")

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = FormLogin()
    print("Hi there")
    print(form.data)
    validate = form.validate_on_submit()
    print(validate)
    if form.validate_on_submit():
        print("It did validate")
        return handle_login(form)

    return render_template("login.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


if __name__ == "__main__":
    app.run(debug=True)
