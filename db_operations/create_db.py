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