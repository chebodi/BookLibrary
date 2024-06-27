class LibraryItemError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


class BookAlreadyBorrowedError(LibraryItemError):
    message = "This book is already borrowed."


class BookNotBorrowedError(LibraryItemError):
    message = "This book was not borrowed."


class DuplicateBookError(LibraryItemError):
    message = "This book is already exist in library."


class BookNotFoundError(LibraryItemError):
    message = "Book not found in the library."


class LibraryItemError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


class BookAlreadyBorrowedError(LibraryItemError):
    message = "This book is already borrowed."


class BookNotBorrowedError(LibraryItemError):
    message = "This book was not borrowed."


class DuplicateBookError(LibraryItemError):
    message = "This book is already exist in library."


class BookNotFoundError(LibraryItemError):
    message = "Book not found in the library."
