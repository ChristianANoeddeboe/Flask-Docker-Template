import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={'autoflush': False})

class Config(object):
    # The reason for this URI https://stackoverflow.com/questions/53024891/modulenotfounderror-no-module-named-mysqldb/54031440
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}/{os.getenv("MYSQL_DB")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False