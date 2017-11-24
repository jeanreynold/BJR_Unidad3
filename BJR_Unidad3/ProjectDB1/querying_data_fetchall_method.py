# BATALIEN Jean Reynold
# Grupo: GITI9072

import psycopg2
from config import config


def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_parts()
    # The number of parts: 6
    (4, 'Antenna')
    (5, 'Home Button')
    (6, 'LTE Modem')
    (1, 'SIM Tray')
    (2, 'Speaker')
    (3, 'Vibrator')

