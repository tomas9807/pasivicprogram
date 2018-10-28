from . import app
from flask import render_template,request,redirect,flash
from werkzeug.utils import secure_filename
import os
def allowed_file(path):
    return '.' in path and str(path).rsplit(r'.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']




@app.route('/')
def home():
    title = 'home'
    return render_template('base.html',**locals())

@app.route('/archivos', methods=['POST','GET'])
def archivos():
    title = 'ingresar archivos'
    if request.method=='POST':
        print(request.form)
        return redirect(request.url)
            
    return render_template('ingresar_archivos.html',title=title)
