#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.data.new(self)

    def __str__(self):
        """ String """
        return ('[' + type(self).__name__ + '] (' + str(self.id) +
                ') ' + str(self.__dict__))

    def save(self):
        """ save function """
        self.updated_at = datetime.datetime.now()
        models.data.save()

    def to_dict(self):
        """ Return a dictonary """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
