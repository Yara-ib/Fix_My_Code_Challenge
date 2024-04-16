#!/usr/bin/python3
""" Square Module """


if __name__ == "__main__":
    class Square():
        """Square Class """

        def __init__(self, *args, **kwargs):
            """ Initialization for instances """
            for key, value in kwargs.items():
                setattr(self, key, value)

        def area_of_my_square(self):
            """ Area of the square """
            return self.width ** 2

        def perimeter_of_my_square(self):
            """ Perimeter of the Square """
            return (self.width * 4)

        def __str__(self):
            """ Returning String format """
            return "{}/{}".format(self.width, self.width)

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
