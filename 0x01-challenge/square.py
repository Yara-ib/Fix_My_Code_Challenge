#!/usr/bin/python3
""" Square Module """


if __name__ == "__main__":
    class square():
        """Square Class """
        width = 0

        def __init__(self, *args, **kwargs):
            """ Initialization for instances """
            for key, value in kwargs.items():
                setattr(self, key, value)

        def area_of_my_square(self):
            """ Area of the square """
            return self.width * self.width

        def PermiterOfMySquare(self):
            """ Perimeter of the Square """
            return (self.width * 4)

        def __str__(self):
            """ Returning String format """
            return "{}/{}".format(self.width, self.width)

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
