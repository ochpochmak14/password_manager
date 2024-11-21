def create_password_table(connection):
    import psycopg2
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS data(
            id serial,
            app VARCHAR NOT NULL,
            login VARCHAR NOT NULL,
            password VARCHAR NOT NULL
            )""")
    cursor.commit()
    