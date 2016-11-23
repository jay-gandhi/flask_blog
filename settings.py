import os

SECRET_KEY = os.urandom(32)
DEBUG = True
DB_USERNAME='jay_gandhi'
DB_PASSWD=''
DB_NAME='blog'
DB_HOST=os.getenv('IP','0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s"%(DB_USERNAME,DB_PASSWD,DB_HOST,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True