from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.book import Book
from db.db_connection import Db
from db.book_db import *

parser = ArgumentParser(
    usage='python3 cli.py <command> [options]',
    formatter_class=RawTextHelpFormatter
)

subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add', help='Add a book to your library, replace space with underscore.')
add_parser.add_argument('title', help='Title of the book, replace space with underscore.')
add_parser.add_argument('author', help='Author of the book')
add_parser.add_argument('--genre', help='Genre of the book')
add_parser.add_argument('--status', help='Reading status of the book')
add_parser.add_argument('--review', help='Review or comments about the book')
add_parser.add_argument('--copies', type=int, help='Number of copies of the book')

list_parser = subparsers.add_parser('list', help='List all books of your library.')

args = parser.parse_args()

db = Db()
db.create_tables()
if args.command == 'add':
    title = args.title
    author = args.author
    genre = args.genre
    status = args.status
    review = args.review
    copies = args.copies
    book = Book(title, author, genre, status, review, copies)
    insert_book(db, book)
elif args.command == 'remove':
    print("Removing a book...")
elif args.command == 'list':
    books = list_book(db)
    for book in books:
        print(book)
else:
    parser.print_help()

db.close_connection()