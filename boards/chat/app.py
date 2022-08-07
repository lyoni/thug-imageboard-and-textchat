#made by lyoni#0007/github.com/lyoni
from re import T
from flask import Flask, render_template, request, redirect, Response, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    username = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        username = request.form.get("username")
        new_post = Posts(text=text, username=username)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    posts = Posts.query.order_by(Posts.id.desc())
    return render_template("index.html", posts=posts[0:100])

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

