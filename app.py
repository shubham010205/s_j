import os
from flask import Flask, render_template, url_for, send_file
from models import db


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", title="Shubham's Projects")


@app.route("/resume")
def resume():
    image = url_for('static', filename='/pics/self.jpg')
    return render_template("resume.html", title="Shubham's Resume", image=image)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Shubham")


@app.route("/resume/download")
def download():
    path = os.path.join(app.root_path, "static/resume/resume.pdf")
    return send_file(path_or_file=path, as_attachment=True, download_name="Shubham_Joshi_Resume.pdf")
