class Book:
    def __init__(self, title, author, genre='miscellaneous', copies=1, status='unread', review=None, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.review = review
        self.copies = copies

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Status: {self.status}\n"
            f"Review: {self.review}\n"
            f"Number of Copies: {self.copies}"
        )

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
