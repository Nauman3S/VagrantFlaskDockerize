from os import environ
import os
from urllib.parse import quote

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.environ['MARIADB_USER']}:%s@db:3306/{os.environ['MARIADB_DATABASE']}" % quote({os.environ['MARIADB_PASSWORD']})