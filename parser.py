from itertools import izip
import string

ZERO = " _ " + \
       "| |" + \
       "|_|"
ONE = "   " + \
      "  |" + \
      "  |"
TWO = " _ " + \
      " _|" + \
      "|_ "
THREE = " _ " + \
        " _|" + \
        " _|"
FOUR = "   " + \
       "|_|" + \
       "  |"
FIVE = " _ " + \
       "|_ " + \
       " _|"
SIX = " _ " + \
      "|_ " + \
      "|_|"
SEVEN = " _ " + \
        "  |" + \
        "  |"
EIGHT = " _ " + \
        "|_|" + \
        "|_|"
NINE = " _ " + \
       "|_|" + \
       " _|"


NUMBERS_BY_TEXT = {
    ZERO: 0,
    ONE: 1,
    TWO: 2,
    THREE: 3,
    FOUR: 4,
    FIVE: 5,
    SIX: 6,
    SEVEN: 7,
    EIGHT: 8,
    NINE: 9
}

class Parser(object):
    def chunk(self, str, chunk_size=3):
        return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]

    def digit_from(self, text):
        return NUMBERS_BY_TEXT[text]

    def digits_from(self, text_array):
        return [self.digit_from(text) for text in text_array]

    def parse(self, stream):
        result = []
        lines = [iter(stream)] * 4
        for line1, line2, line3, _ in izip(*lines):
            joined = izip(self.chunk(line1.rstrip('\n')), self.chunk(line2.rstrip('\n')), self.chunk(line3.rstrip('\n')))
            result.append(self.digits_from(map(lambda w: string.join(w, ''), list(joined))))
        return result


if __name__ == "__main__":
    import fileinput

    print Parser().parse(fileinput.input())