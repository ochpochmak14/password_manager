import psycopg2
from db_connect import host, user, password, db_name
   
  

connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
with connection.cursor() as cursor:
    cursor.execute("""SELECT version();
                        """)
    print(cursor.fetchone())
      # with con.cursor() as cursor:
      #    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
      #       id serial,
      #       user_name VARCHAR(99) NOT NULL PRIMARY KEY,
      #       user_password VARCHAR NOT NULL,
      #       user_secretcode VARCHAR(99) NOT NULL
      #                   )""")
