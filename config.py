import os



class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','mysql+pymysql://teste:123@localhost/clinica_fap')
    SQLALCHEMY_TRACK_MODIFICATIONS = False