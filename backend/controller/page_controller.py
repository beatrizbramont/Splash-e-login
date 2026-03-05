from flask import Blueprint, render_template

page_bp = Blueprint("pages", __name__)

@page_bp.route("/")
def splash():
    return render_template("index.html")

@page_bp.route("/login")
def login_page():
    return render_template("login.html")

@page_bp.route("/cadastro")
def cadastro_page():
    return render_template("cadastro.html")

@page_bp.route("/otp")
def otp_page():
    return render_template("otp.html")

@page_bp.route("/index")
def index():
    return render_template("home.html")
