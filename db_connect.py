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


def db_create(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
            id serial,
            user_name VARCHAR(99) NOT NULL PRIMARY KEY,
            user_password VARCHAR NOT NULL,
            user_secretcode VARCHAR(99) NOT NULL
                        )"""
        )
    connection.commit()
