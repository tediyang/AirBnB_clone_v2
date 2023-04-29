#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of objectss currently in storage.
            {"<object_name>.<object_id>": object}"""
        # If obj is None do nothing.
        if not cls:
            return FileStorage.__objects
        
        #create a dummy dictionary
        dummy = {}
        # loop into dictionary and check key if class name is present.
        for key, value in FileStorage.__objects.items():
            if cls.__name__ in key:
                dummy[key] = value
        return dummy

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file
            {"<object_name>.<object_id>": {object.to_dict()}}"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            """ Update the dictionary by passing in key:value pairs dict
            of the previously loaded data. """
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def delete(self, obj=None):
        ''' Delete object from the database '''
        # If obj is None do nothing.
        if not obj:
            return

        # Extract data to generate the key.
        key = f'{obj.__class__.__name__}.{obj.id}'
        del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                """ Since the values are saved in FileStorage.__objects as:
                    e.g Place.123456678 : Place 
                    # meaning --- The Place (object has all its attributes/ values)
                    Then we have to load the data into FileStorage by passing
                    {Place.123456678 : Place(**val)} this will call the Place object
                    with it value loaded.
                """
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
        
    def close(self):
        """Close the session."""
        self.reload()