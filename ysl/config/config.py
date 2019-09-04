import os


class Config:
    SYSTEM_NAME = 'Yves-Saint-Laurent'


class TestConfig(Config):
    HOST = ''
    PORT = 5000
    DEBUG = True
    TESTING = True

    #DATABASE_URL = get_db_credential_url('test')
    #로컬테스트용 db url
    DATABASE_URL = 'mysql://admin:20020515@ysl-test.cmdmfdz0ht7a.ap-northeast-2.rds.amazonaws.com:13306/test'
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")
    JWT_REFRESH_TOKEN_EXPIRES = os.getenv("JWT_REFRESH_TOKEN_EXPIRES")
