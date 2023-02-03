class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
             Создание и подготовка к работе объекта "Книга"
             :name: Название книги
             :author: Автор книги
             Примеры:
             # >>> book = Book("I am legend", 'John C.')  # инициализация экземпляра класса
             """
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})."

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
             Создание подкласса "Book": и подготовка к работе объекта "Бумажная книга"
             :name: Название книги
             :author: Автор книги
             :pages: Количество страниц
             Примеры:
             # >>> book1 = PaperBook("I am legend", 'John C.', 300)  # инициализация экземпляра класса
             """
        super().__init__(name, author)

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, pages: int):
        """
                Функция которая проверяет является ли количество страниц числом
                :raise TypeError: Если значение не является числом, то вызывается ошибка
                :raise ValueError: Если значение меньше 0, то вызывается ошибка
                Примеры:
                # >>> paper_book1 = PaperBook('Yellow', 'Martin Cook', 6)
                """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}), " \
               f"pages={self.pages!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
             Создание подкласса "Book": и подготовка к работе объекта "Аудиокнига"
             :name: Название книги
             :author: Автор книги
             :duration: Длительность аудиокниги
             Примеры:
             # >>> book2 = AudioBook("I am legend", 'John C.', 3.6)  # инициализация экземпляра класса
             """
        super().__init__(name, author)
        # self.name = name
        # self.author = author
        self.duration = None
        self.set_duration(duration)

    def set_duration(self, duration: float):
        """
                Функция которая проверяет является ли длительность числом с плав.запятой
                :raise TypeError: Если значение не является числом c плавающей запятой,
                то вызывается ошибка
                Примеры:
                # >>> audio_book1 = AudioBook('Yellow', 6)
                """
        if not isinstance(duration, float):
            raise TypeError("Длительность книги - число с плавающей запятой")
        self.duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}), " \
               f"duration={self.duration!r}"


if __name__ == "__main__":
    # book1 = Book("Python", "Sam Bridges")
    paper_book = PaperBook("Python", "Sam Bridges", 300)
    print(paper_book)
    # print(book1._Book__name)
    # # print(book1._Book__author)
    # print(book1._name)
    # print(book1._author)

    # import doctest
    # doctest.testmod()
