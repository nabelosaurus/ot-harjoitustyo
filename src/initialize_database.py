from database_connection import get_database_connection


def drop_tables(connection):
    """Empty the database

    Args:
        connection: sqlite3.connect-object
    """
    cursor = connection.cursor()
    cursor.execute('''drop table if exists users;''')
    cursor.execute('''drop table if exists logins;''')
    connection.commit()


def create_tables(connection):
    """Create tables needed for application

    Args:
        connection: sqlite3.connect-object
    """
    cursor = connection.cursor()
    cursor.execute(
        '''create table users (id integer primary key, master_password text);''')
    cursor.execute('''create table logins
        (id integer primary key, website text, username text, email text, password text, salt blob);
    ''')
    connection.commit()


def initialize_database():
    """Initializes the database by first dropping, then creating needed tables.
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
