import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 1. This MUST match what you access in __init__.py
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # 2. Other settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False