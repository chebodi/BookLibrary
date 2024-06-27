from enum import Enum
from dataclasses import dataclass
from src.services import exceptions


class Condition(Enum):
    NEW = "New"
    FAIR = "Fair"
    GOOD = "Good"
    OLD = "Old"
    TORN = "Torn"


@dataclass
class LibraryItem:
    title: str
    author: str
    publication_year: int

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")


@dataclass
class Book(LibraryItem):
    is_borrowed: bool = False
    book_condition: Condition = Condition.NEW

    def display_info(self):
        super().display_info()
        print(f"Is Borrowed: {self.is_borrowed}")
        print(f"Condition: {self.book_condition}", '\n')


class Library:
    def __init__(self):
        self.library = []

    def add_items(self, item: LibraryItem):
        for existing_item in self.library:
            if existing_item.title == item.title:
                raise exceptions.DuplicateBookError
        self.library.append(item)

    def remove_items(self, title: str):
        for item in self.library:
            if item.title == title:
                self.library.remove(item)
                return
        raise exceptions.BookNotFoundError

    def borrow_items(self, title: str):
        for item in self.library:
            if isinstance(item, Book) and item.title == title:
                if item.is_borrowed:
                    raise exceptions.BookAlreadyBorrowedError

                else:
                    item.is_borrowed = True
                    return
        raise exceptions.BookNotFoundError

    def return_items(self, title: str):
        for item in self.library:
            if isinstance(item, Book) and item.title == title:
                if item.is_borrowed:
                    item.is_borrowed = False
                    return
                else:
                    raise exceptions.BookNotBorrowedError
        raise exceptions.BookNotFoundError

    def show_available_items(self):
        for item in self.library:
            if isinstance(item, Book) and not item.is_borrowed:
                item.display_info()
