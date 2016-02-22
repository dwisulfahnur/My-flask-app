from flask import Blueprint, render_template, request

home_views = Blueprint('home')

@home_views.route("/")
def home():
    return render_template("helloworld.html")
