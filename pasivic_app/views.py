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
    error_buffer = []
    if request.method=='POST':
       
        
        if not request.files:
            flash('ingrese un archivo')
            return redirect(request.url)
        for file in request.files.getlist("file"):
                if file.filename:
                    if allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                    else:
                        error_buffer.append(f'extension del archivo {file.filename} no permitada solo : .xlsx,.xls y .csv')
        for error in error_buffer:
            flash(error)
        return redirect(request.url)
 
    return render_template('ingresar_archivos.html',title=title)
