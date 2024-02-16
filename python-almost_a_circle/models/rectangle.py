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
        self.__width = value

    @property
    def height(self):
        """getter method :height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method : height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.__y = value

    