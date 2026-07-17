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
    def is_borrowed(self) -> bool:
        return self.__is_borrowed

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
    count = 0
    MAX_BOOKS = 3
    def __init__(self, name: str, card_number:str):
        self.__name = name
        self.__card_number = card_number
        self.__borrowed_books: List[Book] = []
        Reader.count += 1

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
            book.return_book()
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
        book = self.__books[isbn]

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f'Книга "{book.title}" выдана, удаление не возможно!'
            )
        del self.__books[isbn]

    def register_reader(self, reader: Reader) -> None:
        """Регистрация нового читателя."""
        if not isinstance(reader, Reader):
            raise TypeError('Читатель должен быть '
                            'представлен классом "Reader"')
        self.__readers[reader.card_number] = reader

    def unregister_reader(self, card_number: str) -> None:
        """Удаление читателя из библиотеки"""
        if card_number not in self.__readers:
            raise ReaderNotFoundException('Читатель с номером'
                                            f'{card_number} не найден.')
        reader = self.__readers[card_number]
        if reader.borrowed_count > 0:
            raise Exception('нельзя удалить читателя, он не сдал книги')
        del self.__readers[card_number]

    def borrow_book(self, card_number: str, isbn: str) -> None:
        """Выдать книгу читателю."""
        if isbn not in self.__books:
            raise BookNotFoundException(f'Книга с ISBN: {isbn} не найдена')

        book = self.__books[isbn]
        if book.is_borrowed:
            raise BookAlreadyBorrowedException('Книга выдана')

        if card_number not in self.__readers:
            raise ReaderNotFoundException('Читатель с номером'
                                            f'{card_number} не найден.')
        reader = self.__readers[card_number]
        reader.borrow_book(book)
        print(f'Книга {book.title} выдана {reader.name}')

    def return_book(self, card_number: str, isbn: str) -> None:
        """Вернуть книгу в библиотеку."""
        if isbn not in self.__books:
            raise BookNotFoundException(f'Книга с ISBN: {isbn} не найдена')

        book = self.__books[isbn]


        if card_number not in self.__readers:
            raise ReaderNotFoundException('Читатель с номером'
                                          f'{card_number} не найден.')
        reader = self.__readers[card_number]
        reader.return_book(book)
        print(f'Книга {book.title} возвращена читателем {reader.name}')

    def get_available_books(self) -> List[Book]:
        """Список доступных книг."""
        return [book for book in self.__books.values() if not book.is_borrowed]

    def get_debtors(self) -> List[Reader]:
        debtors = []
        now = datetime.now()
        for reader in self.__readers.values():
            overdue_books =[
                book for book in reader.borrowed_books
                if book.due_date < now
            ]
            if overdue_books:
                debtors.append(reader)
        return debtors

    def __str__(self) -> str:
        total_books = len(self.__books)
        available_books = len(self.get_available_books())
        # total_readers = len(self.__readers)
        total_readers = Reader.count
        return (f'Библиотека: {self.__name}\n'
                f'Всего книг: {total_books}\n'
                f'Доступно: {available_books}\n'
                f'Кол-во читателей: {total_readers}\n')


if __name__ == '__main__':
    # Создаем библиотеку
    library = Library('Городская библиотека')
    # Создаем книги
    book1 = Book('Война и мир', 'Лев Толстой', 'isbn-01-922', 1869)
    book2 = Book('Преступление и наказание', 'Фёдр Достоевский', 'isbn-01-923', 1866)
    book3 = Book('Мастер и Маргарита', "Михаил Булгаков", 'isbn-01-924', 1967)
    book4 = Book('Анна Каренина', 'Лев Толстой',  'isbn-01-925', 1877)
    # Добавление книг в библиотеку
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # регистрация читателя
    reader1 = Reader('Иван Иванов', 'LIB-001')
    reader2 = Reader('Петр Петров', 'LIB-005')
    # добавляем читателей в библиотеку
    library.register_reader(reader1)
    library.register_reader(reader2)

    try:
        library.borrow_book('LIB-001', 'isbn-01-922')
        library.borrow_book('LIB-001', 'isbn-01-924')
        library.borrow_book('LIB-005', 'isbn-01-925')

    except BookAlreadyBorrowedException as err:
        print(f'Ошибка:', err)
    except ReaderLimitExceededException as err:
        print(f'Ошибка:', err)
    except ReaderNotFoundException as err:
        print(f'Ошибка:', err)
    except BookNotFoundException as err:
        print(f'Ошибка:', err)

    # Покажем доступные книги
    print(f'Доступные книги: ')
    for book in library.get_available_books():
        print(f' {book}')

    # Возвращаем книгу
    # library.return_book('LIB-001', 'isbn-01-922')

    print(f'Доступные книги: ')
    for book in library.get_available_books():
        print(f' {book}')

    # Информация про библиотеку
    print(f'\n{library}')

    # Покажем информацию о читателе
    print(f'\n{reader1}')
    print(f'Книги "на рукаx": ')
    for book in reader1.borrowed_books:
     print(f'{book}')








