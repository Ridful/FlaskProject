from flask import Blueprint, render_template

views_bp = Blueprint('views', __name__, static_folder="static", template_folder="templates", url_prefix="/")

@views_bp.route("/home")
@views_bp.route("/")
def home():
	return render_template("index.html")

@views_bp.route("/about")
def about():
    return "<p>about page would here</p>"