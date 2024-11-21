import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db_name = os.getenv("db_name")


def db_connect():
    global connection
    connection = psycopg2.connect(
        host=host, user=user, password=password, database=db_name
    )

    return connection


