import sqlite3


class Db:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                genre TEXT,
                                status TEXT,
                                review TEXT,
                                copies INTEGER
                            )''')
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

