import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="passwordDecrypter",
            user="postgres",
            password="rootroot")

        print('connection to the database succeded')
    except (Exception, psycopg2.DatabaseError) as error:
        print('An error has occured, could not connect to the database', error)

    return connection
