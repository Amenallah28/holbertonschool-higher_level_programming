#!/usr/bin/python3
""" an empty class Rectangle """


class Rectangle:
    """this is an empty class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol ="#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):

        """print rectangle with #"""
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                ch += "#" * self.__width + "\n"
            return ch[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
