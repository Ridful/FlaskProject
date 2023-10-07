from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__, static_folder="static", template_folder="templates", url_prefix="/auth")

@auth_bp.route("/")
def admin():
	return "<p>default auth page</p>"

@auth_bp.route("/login")
def login():
	return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    return "<p>logout</p>"