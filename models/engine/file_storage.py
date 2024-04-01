#!/usr/bin/python3
"""Provides a simple storage system for managing and persisting
objects in JSON format."""
import json


def get_class_name_to_class():
    """
    Returns a dictionary mapping class names to their corresponding
    class objects.

    This function is used to avoid circular imports by dynamically
    importing the necessary classes.

    Returns:
        dict: A dictionary where keys are class names and values are
        the corresponding class objects.
    """
    # This function is used to avoid circular import
    from models.base_model import BaseModel
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review

    return {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }


class FileStorage:
    """Handles the storage and retrieval of objects in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Retrieve all stored objects of a specified class or all stored
        objects if no class is specified.

        Args:
            cls (Optional[Type]): A class to filter the stored objects by.

        Returns:
            dict: A dictionary containing all stored objects of the specified
            class or all stored objects if no class is specified.
        """

        if cls is not None:
            cls_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    cls_objects[key] = obj
            return cls_objects

        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: An object to be stored.
        """
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[obj_name] = obj

    def save(self):
        """Save the current state of stored objects to the JSON file."""
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        needed_clss = get_class_name_to_class()
        try:
            with open(self.__file_path, 'r') as f:
                json_file = json.load(f)
            for key in json_file:
                class_name = json_file[key]["__class__"]
                obj_dict = json_file[key]
                self.__objects[key] = needed_clss[class_name](**obj_dict)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete a specified object from storage.

        Args:
            obj (Optional[object]): The object to delete from storage.
        """
        if obj is not None:
            obj_name = f'{obj.__class__.__name__}.{obj.id}'
            if obj_name in self.__objects:
                self.__objects.pop(obj_name)

    def close(self):
        """Method for deserializing the JSON file to objects."""
        self.reload()

    def get(self, cls, id):
        """
        Retrieve one object of a class.

        Args:
            cls: Class of the object.
            id: Id of the object.

        Returns:
            The object based on the class and its ID, or None if not found.
        """
        all_objects = self.all(cls)
        for obj in all_objects.values():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage.

        Args:
            cls: Class of the objects (optional).

        Returns:
            The number of objects in storage matching the given class.
            If no class is passed, returns the count of all objects in storage.
        """
        return len(self.all(cls))
