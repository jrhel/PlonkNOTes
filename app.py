from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from logic import logic
import config

app = Flask(__name__)
app.secret_key = config.get_session_key()
logic.initialize_logic()

@app.route("/")
def index():
    if "username" in session.keys():
        return redirect("/user_page")
    else:
        return render_template("index.html")
    
@app.route("/sign_up")
def sign_up():
    return render_template("sign_up/index.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:        
        return "Passwords do not match!"
    else:
        logic.create_user(username, password1)
        session["username"] = username
        return redirect("/user_page")

@app.route("/user_page")
def user_page():
    return render_template("user_page/index.html")

@app.route("/sign_out", methods=["POST"])
def sign_out():
    session.clear()
    return redirect("/")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    if logic.verify_login(username, password):
        session["username"] = username
        return redirect("/user_page")
    else:
        print("Invalid credentials!")
        return redirect("/")
