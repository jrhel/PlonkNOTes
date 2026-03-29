from flask import Flask
from flask import render_template
from flask import session
import config

app = Flask(__name__)
app.secret_key = config.get_session_key()

@app.route("/")
def index():
    if "username" in session.keys():
        return redirect("/user_page")
    else:
        return render_template("index.html")
    
@app.route("/sign_up")
def sign_up():
    return render_template("sign_up/index.html")
