class Config:
    # FLASK_DEBUG = True
    # DEVELOPMENT = True
    SECRET_KEY = 'temporary'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./testdb.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
