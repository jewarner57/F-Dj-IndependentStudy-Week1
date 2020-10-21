from flask import Blueprint, render_template

party = Blueprint("party", __name__,
                  template_folder="templates", url_prefix="/party")


@party.route("/")
def home():
    return render_template("home.html")


@party.route("/about")
def about():
    return render_template("about.html")


@party.route("/contact")
def contact():
    return render_template("contact.html")
