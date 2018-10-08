"""
    Description:    this is a flask application whose purpose is to be
                    a book search engine, review and API provider web
                    application. It is my implementation for CS50's
                    Web Programming with Python and JavaScript's
                    project1. It is my hope that I met all the
                    stipulations and expectations provided by the
                    project's page.

    Project Page:   https://docs.cs50.net/web/2018/w/projects/1/project1.html

    Author:         Igor Matheus Souza Moreira (imatheussm)
    Linkin Profile: https://linkedin.com/in/imatheussm/
    E-mail:         mailto://imatheus.sm@gmail.com
"""

# Import modules in a partial or complete fashion for later use
import os

from flask import Flask, session, render_template, url_for, redirect, request, flash
from flask_session import Session
from flask_login import LoginManager, login_required, login_user, current_user
from flask_moment import Moment
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from helpers import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "3@F[!VBN.=_7)P}a9LCrLf(_gis_`^b3l`Ax/ZM4e&}|+wz|(jwr-ifGUwFX?)m$"
Session(app)

# Initialize flask-moment
moment = Moment(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Define login manager and its configurations
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/api/<int:isbn>")
def api(isbn):
    """
        Description:    API route, where the stipulated information shall
                        be returned in a JSON object.
    """
    pass


@app.route("/")
def index():
    """
        Description:    shows default index page (prior to login).
    """
    return render_template("index.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    """
        Description:    shows login page on GET and deals with submitted
                        information on POST.
    """
    
    if request.method == "POST":
        pass
    # User did not submit a form
    else:
        return render_template("login.html")


@app.route("/recover", methods = ["GET", "POST"])
def recover():
    """
        Description:    shows recover page on GET and deals with
                        submitted information on POST.
    """
    if request.method == "POST":
        pass
    else:
        pass


@app.route("/register", methods = ["GET", "POST"])
def register():
    """
        Description:    shows register page on GET and deals with
                        submitted information on POST.
    """
    if request.method == "POST":
        pass
    else:
        return render_template("register.html")