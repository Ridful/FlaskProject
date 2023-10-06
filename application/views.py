from application import app
from application import render_template


@app.route("/")
def home():
	return render_template("index.html")



