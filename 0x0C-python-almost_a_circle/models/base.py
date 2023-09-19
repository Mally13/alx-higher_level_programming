#!/usr/bin/python3
# base.py

"""Defines class Base"""
import json
import csv
import turtle


class Base:
    """
    class base that has:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries from a JSON string.
        Args:
            json_string (str): A string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates and returns an instance with attributes set from a dictionary.
        Args:
            dictionary (dict): A dictionary containing attribute values.
        """
        if cls.__name__ == "Rectangle":
            d_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            d_instance = cls(1)
        else:
            return None

        d_instance.update(**dictionary)
        return d_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                if not json_data:
                    return []
                else:
                    list_dict = cls.from_json_string(json_data)
                    instances = [cls.create(**d) for d in list_dict]
                    return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to a CSV file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        if len(row) == 5:
                            instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[0])
                                )
                        else:
                            instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4])
                                )
                    elif cls.__name__ == "Square":
                        if len(row) == 4:
                            instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[0])
                                )
                        else:
                            instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3])
                                )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Create a Turtle Screen
        screen = turtle.Screen()
        screen.title("Draw Rectangles and Squares")

        # Create a Turtle object
        pen = turtle.Turtle()
        pen.speed(1)

        # Draw Rectangles
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        # Draw Squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        # Close the window on click
        screen.exitonclick()
