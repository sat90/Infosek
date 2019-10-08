import os

# contains application-wide configuration, and is loaded in __init__.py

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret' # TODO: Use this with wtforms
    DATABASE = 'database.db'
    UPLOAD_PATH = 'app/static/uploads'
<<<<<<< Updated upstream
    ALLOWED_EXTENSIONS = {} # Might use this at some point, probably don't want people to upload any file type
=======
    ALLOWED_EXTENSIONS = {'bmp', 'gif', 'jpeg', 'jpg', 'tex',
    'doc', 'docx', 'odt', 'txt', 'pdf', 'png', 'rtf'} # Only allowing some file types.
>>>>>>> Stashed changes
