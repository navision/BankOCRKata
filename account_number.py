from numbers import Number


class AccountNumber(object):
    def __init__(self, digits):
        self.digits = digits

    def checksum(self):
        # dX where X is counted right to left
        # (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0
        result = 0
        position = 1
        while position <= len(self.digits):
            result += (self.digits[-position] * position)
            position += 1
        return result

    def is_valid(self):
        if not self.is_legible(): return False
        return self.checksum() % 11 == 0

    def is_legible(self):
        for i in self.digits:
            if not isinstance(i, Number):
                return False
        return True

    def as_string(self):
        return ''.join(map(lambda d: '?' if d is None else str(d), self.digits))

    def __eq__(self, other):
        if other.__class__ != self.__class__: return False
        return self.digits == other.digits

    def __hash__(self):
        return hash(self.digits)

    def __repr__(self):
        return "AccountNumber(%s)" % self.digits
