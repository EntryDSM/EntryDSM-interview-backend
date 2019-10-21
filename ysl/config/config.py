import os
from datetime import timedelta


class Config:
    SYSTEM_NAME = 'Yves-Saint-Laurent'

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=20)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    DATABASE_URL = os.getenv("DATABASE_URL")


class TestConfig(Config):
    HOST = ''
    PORT = 5000
    DEBUG = True


class ProdConfig(Config):
    HOST = '0.0.0.0'
    PORT = 8084
    DEBUG = False
