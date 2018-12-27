from __future__ import division


class Rational(object):
    def __init__(self, numer: int, denom: int):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other: object):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        rational = Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)
        rational.reduce()
        return rational

    def __sub__(self, other):
        rational = Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)
        rational.reduce()
        return rational

    def __mul__(self, other):
        rational = Rational(self.numer * other.numer, self.denom * other.denom)
        rational.reduce()
        return rational

    def __truediv__(self, other):
        rational = Rational(self.numer * other.denom, self.denom * other.numer)
        rational.reduce()
        return rational

    def __abs__(self):
        if self.numer < 0:
            self.numer *= -1
        if self.denom < 0:
            self.denom *= -1
        return self

    def __pow__(self, power):
        if power == 0:
            return Rational(1, 1)

        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base) -> float:
        if self.numer == 0:
            return 1.0

        return base ** (self.numer / self.denom)

    def reduce(self):
        if self.numer == 0:
            self.denom = 1
            return

        if self.denom < 0 < self.numer:
            self.denom *= -1
            self.numer *= -1

        if self.denom < 0 and self.numer < 0:
            self.denom *= -1
            self.numer *= -1

        gcd = self.gcd(self.numer.__abs__(), self.denom.__abs__())
        self.numer = int(self.numer / gcd)
        self.denom = int(self.denom / gcd)

    # https://en.wikipedia.org/wiki/Greatest_common_divisor#Binary_method
    @staticmethod
    def gcd(a: int, b: int) -> int:
        d = 0
        while (a & 1) == 0 and (b & 1) == 0:
            a = a >> 1
            b = b >> 1
            d += 1

        while a != b:
            if (a & 1) == 0:
                a = a >> 1
            elif (b & 1) == 0:
                b = b >> 1
            elif a > b:
                a = (a - b) >> 1
            else:
                b = (b - a) >> 1

        return 2 ** d * a
