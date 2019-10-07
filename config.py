import os

# contains application-wide configuration, and is loaded in __init__.py

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret' # TODO: Use this with wtforms
    DATABASE = 'database.db'
    UPLOAD_PATH = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'gif', 'jpeg', 'jpg','png'} # Only allowing some file types.
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
