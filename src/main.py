from services.library import Library, Book, Condition

if __name__ == "__main__":
    library = Library()

    book1 = Book(title="About Cat", author="Masha Kulka", publication_year=2001)
    book2 = Book(title="Basic C++", author="Donald Trump", publication_year=2021)
    book3 = Book(title="Kolobok", author="Babushka Gala", publication_year=2000, book_condition=Condition.GOOD)
    book4 = Book(title="1939", author="Adolph Hitler", publication_year=1945, book_condition=Condition.OLD)

    library.add_items(book1)
    library.add_items(book2)
    library.add_items(book3)
    library.add_items(book4)

    library.remove_items("Basic C++")
    library.remove_items("1939")

    print("\nAvailable books in the library:")
    library.show_available_items()
