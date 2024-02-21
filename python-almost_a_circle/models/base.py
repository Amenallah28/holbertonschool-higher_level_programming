#!/usr/bin/python3
"""  bismellah : the base class """

import json


class Base:
    """belehy ikhdem"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representation json_string:"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(5, 5)
        elif cls is Square:
            dummy = Square(5)
        else:
            dummy = None
        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                cont = f.read()
                list = cls.from_json_string(cont)
                instan_l = []
                for dict in list:
                    instan = cls.create(**dict)
                    instan_l.append(instan)
                return instan_l
        except FileNotFoundError:
            return []
