import sqlite3

from book_keeping_cli.model.book import Book


def book_exists(db, title, author):
    try:
        db.cursor.execute('SELECT * FROM book WHERE title = ? AND author = ?', (title, author))
        row = db.cursor.fetchone()
        if row:
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def insert_book(db, book):
    if book_exists(db, book.title, book.author):
        print(f"Book '{book.title}' by {book.author} already exists.")
        return
    else:
        try:
            db.cursor.execute('''INSERT INTO book (title, author, genre, copies, status, review)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                              (book.title, book.author, book.genre, book.copies, book.status, book.review))
            db.conn.commit()
            print(f"Book '{book.title}' by {book.author} has been added.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


def list_book(db):
    try:
        db.cursor.execute('SELECT * FROM book')
        rows = db.cursor.fetchall()
        books = []
        for row in rows:
            book = Book(*row)  # Unpack the tuple directly into the Book constructor
            books.append(book)
        return books
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def remove_book(db, title, author):
    if not book_exists(db, title, author):
        print(f"Book '{title}' by {author} doesn't exist.")
        return
    else:
        try:
            db.cursor.execute('DELETE FROM book WHERE title = ? AND author = ?', (title, author))
            db.conn.commit()
            print(f"Book '{title}' by {author} has been removed.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
