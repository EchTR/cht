# github.com/echtr
import logging
from cv2 import log
from flask import Flask, request, redirect, session,  render_template, url_for
import os
import sqlite3
from modules.db_connection import get, post
from modules.get_time import get_time
from modules.get_posts import get_posts
import datetime

cht = Flask(__name__)
cht.secret_key = os.urandom(24)
cht.permanent_session_lifetime = datetime.timedelta(minutes=5)

usernames = [x[0] for x in get()]
emails = [x[1] for x in get()]
passwords = [x[2] for x in get()]

@cht.route("/")
def index_page():
    if "user" in session:
        loggined = True
        show_posts = get_posts("new")
        return render_template("index.html", log_status=loggined, user_status = session["user"], posts = show_posts)
    else:
        loggined = False
        return render_template("index.html", log_status=loggined, user_status = None)
    

@cht.route("/register", methods=["GET", "POST"])
def register_page():
    usernames = [x[0] for x in get()]
    emails = [x[1] for x in get()]
    passwords = [x[2] for x in get()]
    if request.method == "GET":
        if "user" in session: return redirect(url_for("index_page"))
        else: return render_template("register.html", log_status = False)
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if username.lower() in [i.lower() for i in usernames] or email.lower() in [i.lower() for i in emails]: return "That username/ email is already exists..."
        else:
            post(username, email, password)
            session.permanent = True
            session["user"] = (username, email, password) 
            return redirect(url_for("index_page"))

@cht.route("/login", methods = ["GET", "POST"])
def login_page():
    usernames = [x[0] for x in get()]
    emails = [x[1] for x in get()]
    passwords = [x[2] for x in get()]
    if request.method == "GET":
        if "user" in session:
            return redirect(url_for("index_page"))
        else: 
            loggined = False
            return render_template("login.html", log_status=loggined)
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if username.lower() in [i.lower() for i in usernames]:
            index = usernames.index(username)
            if passwords[index] == password:
                session["user"] = (username, emails[index], password)
                return redirect(url_for("index_page"))
            else:
                return "wrong username or password"
        else:
            return "we cant found your username in our database. please check!"

@cht.route("/logout")
def logout_page(): 
    if "user" in session:
        session.pop("user", None)
        loggined = False
    return redirect(url_for("login_page"))

@cht.route("/myposts")
def myposts_page():
    if "user" in session:
        user_posts = get_posts("new", user = str(session["user"][0]))
        up_length = len(user_posts)
        print(user_posts)
        print(up_length)
        return render_template("myposts.html", posts = user_posts, upl = up_length, user_status = session["user"], log_status=True)
    else:
        return redirect(url_for("login_page"))
cht.run(debug=True)