import doctest


class Book:
    def __init__(self, pages: int, author: str):
        self.pages = pages
        self.author = author
        self.get_pages(pages)

    def get_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Значение не является численным")
        if pages < 0:
            raise ValueError("Значение страниц не может быть меньше нуля")

    def __str__(self):
        return f'Значение страниц книги: {self.pages}, Автор: {self.author}'


class Car:
    def __init__(self, color: str, size: int):
        self.color = color
        self.size = size
        self.get_color(color)

    def get_color(self, color: str):
        # color = input("Введите цвет\n")
        return color

    def __str__(self):
        return f'Цвет машины: {self.color}, Размер: {self.size}'


class Table:
    def __init__(self, color: str, hight: int):
        self.hight = hight
        self.color = color
        self.get_hight(hight)

    def get_hight(self, hight: int):
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
