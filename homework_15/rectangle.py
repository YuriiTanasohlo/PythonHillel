class Rectangle:

    __width: float
    __height: float

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other: "Rectangle"):
        return self.get_square() == other.get_square()

    def __add__(self, other: "Rectangle"):
        sum_square = self.get_square() + other.get_square()
        sum_height = sum_square / self.width
        return Rectangle(self.width, sum_height)

    def __mul__(self, n: float):
        multiplication_square = self.get_square() * n
        multiplication_height = multiplication_square / self.width
        return Rectangle(self.width, multiplication_height)

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"
