#!/usr/bin/python3
""" Square Module """


class Square():
    """Square Class """

    width = 0

    def __init__(self, *args, **kwargs):
        """ Initialization for instances """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the Square """
        return (self.width * 4)

    def __str__(self):
        """ Returning String format """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
