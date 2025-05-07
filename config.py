import os

class Config:
    # Flask
    SECRET_KEY = "secret_key"
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True 