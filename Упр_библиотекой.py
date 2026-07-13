from typing import List, Tuple, Union, Optional, Dict
from datetime import datetime, timedelta

class BookNotFoundException(Exception):
    """Книга не найдена"""
    pass


class BookAlreadyBorrowedException(Exception):
    """Книга уже выдана"""
    pass


class ReaderLimitExceededException(Exception):
    """Читатель достиг лимита книг"""


class ReaderNotFoundException(Exception):
    """Читатель не найден"""


class Book:
    """Класс, представляющий книгу"""
    def __init__(self, title: str, author: str, isbn: str, year: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__is_borrowed = False
        self.__borrowed_by: Optional['Reader'] = None
        self.__due_date: Optional[datetime] = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def is_borrowed_by(self) -> bool:
        return self.__borrowed_by

    @property
    def due_date(self) -> Optional[datetime]:
        return self.__due_date

    def borrow(self, reader: 'Reader') -> None:
        """Выдать книгу читателю"""
        if self.__borrowed_by:
            raise BookAlreadyBorrowedException(f'Книга "{self.__title}" уже выдана')
        self.__is_borrowed = True
        self.__borrowed_by = reader
        self.__due_date = datetime.now() + timedelta(days=14)  # 14 дней на возврат

    def return_book(self) -> None:
        """Вернуть книгу в библиотеку"""
        self.__is_borrowed = False
        self.__borrowed_by = None
        self.__due_date = None

    def __str__(self) -> str:
        status = "Доступна" if not self.__is_borrowed else f'Выдана {self.__borrowed_by}'
        return f'"{self.__title}" {self.__author} ({self.__year}) - {status}'

    def __repr__(self) -> str:
        return f'Название книги: {self.__title}, Автор: {self.__author}'


class Reader:
    """Класс представляющий читателя"""
    MAX_BOOKS = 3
    def __init__(self, name: str, card_number:str):
        self.__name = name
        self.__card_number = card_number
        self.__borrowed_books: List[Book] = []

    @property
    def name(self) -> str:
        return self.__name
    @property
    def card_number(self) -> str:
        return self.__card_number

    @property
    def borrowed_books(self) -> List[Book]:
        """Возвращает копию списка для защиты инкапсуляции"""
        return self.__borrowed_books.copy()

    @property
    def borrowed_count(self) -> int:
        return len(self.__borrowed_books)

    def borrow_book(self, book: Book) -> None:
        """Взять книгу"""
        if len(self.__borrowed_books) >= self.MAX_BOOKS:
            raise ReaderLimitExceededException(
                f'Читатель {self.__name} достиг лимита в {self.MAX_BOOKS} книги'
            )
        book.borrow(self)
        self.__borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        """Вернуть книгу"""
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)

    def __str__(self):
        books_count = len(self.__borrowed_books)
        return f"Читатель {self.__name} (№{self.__card_number}), книг на руках - {books_count}"

    def __repr__(self):
        return f'Читатель {self.__name}, card (№{self.__card_number})'


class Library:
    """Класс, представляющий библиотеку"""
    def __init__(self, name: str):
        self.__name = name
        self.__books: Dict[str, Book] = {}  # ISBN -> Book
        self.__readers: Dict[str, Reader] = {}  # card_number -> Reader

    @property
    def name(self) -> str:
        return self.__name

    def add_book(self, book: Book) -> None:
        """Добавить книгу в библиотеку"""
        if not isinstance(book, Book):
            raise TypeError('book должен принадлежать классу Book')
        self.__books[book.isbn] = book

    def remove_book(self, isbn: str) -> None:
        """Удаление книги из библиотеки"""
        if isbn not in self.__books:
            raise BookNotFoundException(f'Книга с ISBN: {isbn} не найдена')





book1 = Book('Война и мир 1', 'Лев Толстой', 'isbn-01-922', 1869)
book2 = Book('Война и мир 2', 'Лев Толстой', 'isbn-01-923', 1869)
print(book1)
books = [book1, book2]
print(books)