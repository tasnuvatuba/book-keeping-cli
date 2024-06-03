# Book Keeping CLI

## Overview
The Book Keeping CLI is a command-line application that allows users to manage their personal library by adding, removing, and listing books. It provides a simple and efficient way to keep track of your reading progress and book collection.

## Features
- **Add Books**: Add a new book to your library with details such as title, author, genre, reading status, review, and number of copies.
- **List Books**: View a list of all books in your library along with their details.
- **Remove Books**: Remove a book from your library by specifying its title and author.

## Installation
1. Clone the repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd book-keeping-cli
    ```

[//]: # (3. Install the dependencies:)

[//]: # ()
[//]: # (    ```)

[//]: # (    pip install -r requirements.txt)

[//]: # (    ```)

## Usage
To use the Book Keeping CLI, run the `cli.py` script followed by the desired command and options:

### Commands:
- `add`: Add a book to your library.
- `list`: List all books in your library.
- `remove`: Remove a book from your library.

### Options:
- `add` Command:
    - `title`: Title of the book (replace spaces with underscores or use quotation marks).
    - `author`: Author of the book (replace spaces with underscores or use quotation marks).
    - `--genre`: Genre of the book (choose from Fiction, Non-Fiction, Sci-Fi, Miscellaneous).
    - `--status`: Reading status of the book (choose from Unread, Reading, Completed).
    - `--review`: Review or comments about the book (replace spaces with underscores or use quotation marks).
    - `--copies`: Number of copies of the book.

- `remove` Command:
    - `title`: Title of the book to remove (replace spaces with underscores or use quotation marks).
    - `author`: Author of the book (replace spaces with underscores or use quotation marks).
## Examples
- Add a book to the library:
    ```
    python3 cli.py add "Harry Potter and the Philosopher's Stone" "J.K. Rowling" --genre "Fiction" --status "Reading" --review "Enjoyable read" --copies 1
    ```

- List all books in the library:
    ```
    python3 cli.py list
    ```

- Remove a book from the library:
    ```
    python3 cli.py remove "Harry_Potter_and_the_Philosopher's_Stone" "J.K._Rowling"
    ```

