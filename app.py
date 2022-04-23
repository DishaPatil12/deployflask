
# try:
#     from flask import Flask
#     from flask import request, redirect, url_for, render_template
#     from flask_wtf.file import FileField
#     from wtform import SubmitField
#     from flask_api import Form
#     import sqlite3
#     print("all modules loaded......")
# except:
#     print("Some Module are missing")



# app = Flask(__name__)
# app.config["SECRET_KEY"] ="secret"

# @app.route('/', methods =["GET", "POST"])
# def index():
#     form =UploadForm()
#     return render_template("home.html", form=form)


# class UploadForm(Form):
#     file = FileField()
#     submit = SubmitField("submit")
    

# if __name__ =="__main__":
#     app.run(debug=True)

from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
    
app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLD = '/Users/Lenovo/New folder'
# UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY']='supersecretkey'

app.config['UPLOAD_FOLDER']='static/files'


class UploadFileForm(FlaskForm):
    file= FileField("File")
    submit = SubmitField("Upload File")

@app.route('/', methods =["GET", "POST"])
@app.route('/home', methods =["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file= form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File has be uploaded"
    # return "Hello from flask"
    return render_template('home.html', form=form)

if __name__ =="__main__":
    app.run(debug=True)