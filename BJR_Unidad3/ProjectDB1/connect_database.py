#BATALIEN Jean Reynold
#Grupo: GITI9072

import psycopg2
from config import config

def connect():
    """Connect to the Postgresql database server"""
    connection = None

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        # create cursor
        cursor = connection.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        # display the PostgreSQL datbase sever version
        db_version =cursor.fetchone()
        print(db_version)

        # close the commnuication with the PostgreSQL
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
if __name__=='__main__':
    connect()
