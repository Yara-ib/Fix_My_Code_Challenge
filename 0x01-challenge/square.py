#!/usr/bin/python3
""" Square Module """


class Square():
    """Square Class """
    width = 0
    # height = 0

    def __init__(self, width=1):
        """ Initialization for instances """
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width ** 2

    def perimeter_of_square(self):
        """ Perimeter of the Square """
        return (self.width * 4)

    def __str__(self):
        """ Returning String format """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_square())
