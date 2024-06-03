from argparse import ArgumentParser, RawTextHelpFormatter
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db_connection import Db
from db.book_db import *

parser = ArgumentParser(
    #usage='python3 cli.py <command> [options]',
    formatter_class=RawTextHelpFormatter
)

subparsers = parser.add_subparsers(dest='command')
add_parser = subparsers.add_parser('add', help='Add a book to your library, replace space with underscore')
add_parser.add_argument('title', help='Title of the book, replace spaces with underscores or use quotation mark')
add_parser.add_argument('author', help='Author of the book, replace spaces with underscores or use quotation mark')
add_parser.add_argument('--genre', choices=['Fiction', 'Non-Fiction', 'Sci-Fi', 'Miscellaneous'], help='Genre of the book')
add_parser.add_argument('--status', choices=['Unread', 'Reading', 'Completed'], help='Reading status of the book')
add_parser.add_argument('--review', help='Review or comments about the book, replace spaces with underscores or use '
                                         'quotation mark')
add_parser.add_argument('--copies', type=int, help='Number of copies of the book')

list_parser = subparsers.add_parser('list', help='List all books of your library.')

remove_parser = subparsers.add_parser('remove', help='Remove a book by its title and author from your library')
remove_parser.add_argument('title', help='Title of the book, replace space with underscore.')
remove_parser.add_argument('author', help='Author of the book, replace space with underscore.')

args = parser.parse_args()

db = Db()
db.create_tables()
header = (
    f"{'Id':<3} | "
    f"{'Title':<15} | "
    f"{'Author':<15} | "
    f"{'Genre':<10} | "
    f"{'Copies':<7} | "
    f"{'Status':<10} | "
    f"{'Review':<25}"
)

if args.command == 'add':
    id = None
    title = args.title
    author = args.author
    genre = args.genre
    status = args.status
    review = args.review
    copies = args.copies
    book = Book(id, title, author, genre, copies, status, review)
    if book.is_valid():
        insert_book(db, book)
elif args.command == 'remove':
    title = args.title
    author = args.author
    remove_book(db, title, author)
elif args.command == 'list':
    books = list_book(db)
    if len(books) == 0:
        print("No books to show. Add your first book to the library!")
    for book in books:
        print(book)
else:
    parser.print_help()

db.close_connection()
