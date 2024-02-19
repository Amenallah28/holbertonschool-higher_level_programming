#!/usr/bin/python3
""" bismellah : class Rectangle """
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method :width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method : width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method :height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method : height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returning the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                for i in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update1(self, id=None, width=None, height=None, x=None, y=None):
        """task 8: method to update instance attributes via *args only"""
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        """task 9 : update instance attribute via *args and **kwargs"""
        if args:
            self.update1(*args)
        elif kwargs:
            self.update1(**kwargs)

    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
