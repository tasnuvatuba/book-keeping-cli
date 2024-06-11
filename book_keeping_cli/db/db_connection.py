import sqlite3


class DbConnection:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                genre TEXT,
                                copies INTEGER,
                                status TEXT,
                                review TEXT
                            )''')
        self.conn.commit()

    def delete_all_tables(self):
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = self.cursor.fetchall()
            for table in tables:
                table_name = table[0]
                self.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            self.conn.commit()
            print("All tables have been deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
