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
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


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
        # self.name = name
        # self.author = author
        self.get_pages(pages)  # атрибут подкласса "Бумажная книга"

    def get_pages(self, pages: int):
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

    # def __str__(self):
    #     return f"Книга {self._name}. Автор {self._author}"
    #     # super().__str__()


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
        self.get_duration(duration)

    def get_duration(self, duration: float):
        """
                Функция которая проверяет является ли длительность числом с плав.запятой
                :raise TypeError: Если значение не является числом c плавающей запятой,
                то вызывается ошибка
                Примеры:
                # >>> audio_book1 = AudioBook('Yellow', 6)
                """
        if not isinstance(duration, float):
            raise TypeError("Длительность книги - число с плавающей запятой")


def __str__():
    super().__str__()
    # return f"Книга {self._name}. Автор {self._author}"


def __repr__():
    super().__repr__()


if __name__ == "__main__":
    book12 = Book("Python", "Sam Bridges")
    audio_book = AudioBook("Hello", "Mary K.", 3.7)
    paper_book = PaperBook("Mary", "Jake K.", 300)

    print(audio_book.__str__())
    print(paper_book.__str__())

    print(audio_book.__repr__())
    print(paper_book.__repr__())

    # print(book12._Book__name)
    # print(book12._Book__author)
    print(book12._name)
    print(book12._author)

    # print(dir(AudioBook))

    # import doctest
    # doctest.testmod()
