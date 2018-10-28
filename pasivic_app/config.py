import os

class Config():
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),'tmp_files')
    ALLOWED_EXTENSIONS = set(['xls','xlsx','csv'])
    SECRET_KEY = 'nosecret'

