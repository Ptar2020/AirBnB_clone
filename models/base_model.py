#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = created_at

    def __str__(self):
        return type(self.__name__) + str(self.id) + str(self.__dict__)

    def save(self):
        pass

    def to_dict(self):
        pass
