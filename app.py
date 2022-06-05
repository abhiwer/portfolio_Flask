from flask import Flask, render_template, send_file
import requests


app = Flask(__name__)



@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/download')
def download_file():
    path="static/Abhinav_Priyadarshi_CV.pdf"
    return send_file(path, as_attachment=True)



    