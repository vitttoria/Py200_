import doctest


class Book:
    def __init__(self, pages: int, author: str):
        """
             Создание и подготовка к работе объекта "Книга"
             :pages capacity_volume: Объем стакана
             :author occupied_volume: Объем занимаемой жидкости
             Примеры:
             >>> book2 = Book(500, 'John')  # инициализация экземпляра класса
             """
        self.pages = pages
        self.author = author
        self.get_pages(pages)

    def get_pages(self, pages: int):
        """
                Функция которая проверяет являются ли страницы числом
                :raise TypeError: Если значение не является числом, то вызывается ошибка
                :raise ValueError: Если значение отрицательное, то вызывается ошибка
                Примеры:
                >>> book1 = Book(500, 'Mary')
                >>> book.get_pages(-300)
                """
        if not isinstance(pages, int):
            raise TypeError("Значение не является численным")
        if pages < 0:
            raise ValueError("Значение страниц не может быть меньше нуля")

    def __str__(self):
        return f'Значение страниц книги: {self.pages}, Автор: {self.author}'


class Car:
    def __init__(self, color: str, size: int):
        """
             Создание и подготовка к работе объекта "Машина"
             :pages color: Цвет
             :author size: Размер
             Примеры:
             >>> car1 = Car('Yellow', 5)  # инициализация экземпляра класса
             """
        self.color = color
        self.size = size

    def __str__(self):
        return f'Цвет машины: {self.color}, Размер: {self.size}'


class Table:
    def __init__(self, color: str, hight: int):
        """
             Создание и подготовка к работе объекта "Стол"
             :pages color: Цвет
             :author hight: Высота
             Примеры:
             >>> car1 = Car('Yellow', 5)  # инициализация экземпляра класса
             """
        self.hight = hight
        self.color = color
        self.get_hight(hight)

    def get_hight(self, hight: int):
        """
                Функция которая проверяет является ли высота числом
                :raise TypeError: Если значение не является числом, то вызывается ошибка
                :raise ValueError: Если значение отрицательное, то вызывается ошибка
                Примеры:
                >>> table1 = Table('Yellow', 6)
                >>> table1.get_hight(-4)
                """
        if not isinstance(hight, int):
            raise TypeError("Значение не является численным")
        if hight < 0:
            raise ValueError("Значение высоты не может быть меньше нуля")

    def __str__(self):
        return f'Цвет стола: {self.color}, Размер: {self.hight}'


if __name__ == "__main__":
    book = Book(300, "Mary")
    car = Car(input("Введите цвет\n"), 20)
    table = Table("Yellow", 20)

    print(book.__str__())
    print(car.__str__())
    print(table.__str__())

    doctest.testmod()
