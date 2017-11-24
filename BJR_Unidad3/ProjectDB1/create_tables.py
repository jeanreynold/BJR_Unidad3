# BATALIEN Jean Reynold
# Grupo: GITI9072

import psycopg2
from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""

commands =(
    """
    CREATE TABLE log(
    id SERIAL PRIMARY KEY,
    ts TIMESTAMP NOT NULL,
    phrase VARCHAR(128),
    letters VARCHAR(32),
    ip VARCHAR(16),
    browser_string VARCHAR(256) NOT NULL,
    results VARCHAR(64) NOT NULL)""",
    """
    CREATE TABLE vendors(
    vendor_id SERIAL PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL)""",
    """
    CREATE TABLE parts(
    part_id SERIAL PRIMARY KEY,
    part_name VARCHAR(255) NOT NULL)""",
    """
    CREATE TABLE parts_drawing(
    part_id INTEGER PRIMARY KEY,
    file_extension VARCHAR(5) NOT NULL,
    drawing_data BYTEA NOT NULL,
    FOREIGN KEY(part_id)
    REFERENCES parts(part_id)
    ON UPDATE CASCADE ON DELETE CASCADE)""",
    """
    CREATE TABLE vendor_parts(
    vendor_id INTEGER NOT NULL,
    part_id INTEGER NOT NULL,
    PRIMARY KEY(vendor_id, part_id),
    FOREIGN KEY (vendor_id)
    REFERENCES  vendors(vendor_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(part_id)
    REFERENCES parts(part_id)
    ON UPDATE CASCADE ON DELETE CASCADE)""",
)

connection = None
try:
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()
    # create table one by one
    for command in commands:
        cursor.execute(command)
    # close communication with the postgreSQL database server.
    cursor.close()
    #commit the changes
    connection.commit()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()

if __name__=='__main__':
    create_tables()