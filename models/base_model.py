#!/usr/bin/python3
"""This script is the base model"""
"""The base model" script """

import uuid
from datetime import datetime
@@ -8,14 +8,10 @@

class BaseModel:

    """Class from which all other classes will inherit"""
    """ The class inheriter of all other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """Initializing instance attributes
        """

        if kwargs is not None and kwargs != {}:
@@ -35,52 +31,22 @@ def __init__(self, *args, **kwargs):
            storage.new(self)

    def __str__(self):
        """Returns official string representation"""
        """Returns string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        """updating the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        """returns the dictionary holoding all values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
=======
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
