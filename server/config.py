# DB config will go here

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///pizza.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
