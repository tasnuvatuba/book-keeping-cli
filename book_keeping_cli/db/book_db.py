from book_keeping_cli.model.book import Book

def insert_book(db, book):
    db.cursor.execute('''INSERT INTO book (title, author, genre, status, review, copies)
                  VALUES (?, ?, ?, ?, ?, ?)''',
                      (book.title, book.author, book.genre, book.status, book.review, book.copies))
    db.conn.commit()


def list_book(db):
    db.cursor.execute('SELECT * FROM book')
    rows = db.cursor.fetchall()
    books = []
    for row in rows:
        book = Book(*row)  # Unpack the tuple directly into the Book constructor
        books.append(book)
    return books
