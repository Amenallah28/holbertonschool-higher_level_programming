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
        """writes the json string representation"""
        if list_objs is not None:
            list_objs = [objs.to_dictionary() for objs in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representation json_string:"""
        if json_string is None or not json_string:
            return ([])
        else:
            return (json.loads(json_string))
    
