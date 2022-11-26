#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """ User class that inherits BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
