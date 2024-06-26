#!/usr/bin/python3
"""Square Class"""


class Square:
    """a Square class"""

    def __init__(self, *args, **kwargs):
        """making a new instance of Square object"""
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """returns width and height of square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
