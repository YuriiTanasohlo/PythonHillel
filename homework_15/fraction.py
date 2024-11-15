class Fraction:

    __numerator: int
    __denominator: int

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __mul__(self, other: "Fraction"):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __add__(self, other: "Fraction"):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)

    def __sub__(self, other: "Fraction"):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)

    def __eq__(self, other: "Fraction"):
        if self.denominator == other.denominator:
            return self.numerator == other.numerator
        else:
            return self.numerator / self.denominator == other.numerator / other.denominator

    def __gt__(self, other: "Fraction"):
        if self.denominator == other.denominator:
            return self.numerator > other.numerator
        else:
            return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other: "Fraction"):
        if self.denominator == other.denominator:
            return self.numerator < other.numerator
        else:
            return self.numerator / self.denominator < other.numerator / other.denominator

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"