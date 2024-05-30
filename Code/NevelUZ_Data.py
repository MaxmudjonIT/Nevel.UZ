import sqlite3

db_connect = sqlite3.connect('NevelUZData.sqlite3')

db_cursor = db_connect.cursor()


def create_basket_table():
    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS basket (id INTEGER PRIMARY KEY, title TEXT, price INTEGER, quantity INTEGER)""")
    db_connect.commit()



def create_favorites_table():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY, title TEXT, price INTEGER, quantity INTEGER)
    """)
    db_connect.commit()


create_favorites_table()
create_basket_table()
