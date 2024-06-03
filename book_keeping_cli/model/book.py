class Book:
    def __init__(self, id, title, author, genre, copies, status, review):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre if genre else 'Miscellaneous'
        self.status = status if status else 'Unread'
        self.review = review
        self.copies = copies if copies else 1

    def __str__(self):
        id = self.id if self.id else ''
        title = self.title if self.title else ''
        author = self.author if self.author else ''
        genre = self.genre if self.genre else ''
        status = self.status if self.status else ''
        review = self.review if self.review else ''
        copies = self.copies if self.copies is not None else 0

        return (
            f"Id: {id} | "
            f"Title: {title:15} | "
            f"Author: {author:15} | "
            f"Genre: {genre:10} | "
            f"Copies: {copies} | "
            f"Status: {status:5} | "
            f"Review: {review:25}"
        )

    def is_valid(self):
        if self.copies <= 0:
            print("Enter positive number of copies.")
            return False
        elif self.status != 'Completed' and self.review:
            print("You have to complete the book before writing a review")
            return False
        return True

    def set_genre(self, genre):
        self.genre = genre

    def set_status(self, status):
        self.status = status

    def set_review(self, review):
        self.review = review

    def set_copies(self, copies):
        self.copies = copies

    def increment_copies(self, amount=1):
        self.copies += amount

    def decrement_copies(self, amount=1):
        if self.copies - amount >= 0:
            self.copies -= amount
            return True
        else:
            return False
