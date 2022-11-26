#!/usr/bin/python3
import cmd
import time
import sys
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity
import models
"""The console class"""


class HBNBCommand(cmd.Cmd):
    """The HBNB main class"""
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel,
               'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City
               }

    def do_help(self, line):
        """Get help on using the console"""
        text = '''Documented commands (type help < topic > ): \n ========================================\nEOF help  quit\n'''
        print(text, line)

    def do_create(self, line):
        if not line:
            print("**Class name missing**")
        else:
            if line in self.classes:
                get_class = getattr(sys.modules[__name__], line)
                print(get_class().id)
                models.data.save()
            else:
                print("**class doesn't exist**")
        return

    def do_show(self, line):
        """ Method to print instance """
        if len(line) == 0:
            print('** class name missing **')
            return
        elif line.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(line.split()) > 1:
            key = line.split()[0] + '.' + line.split()[1]
            if key in models.data.all():
                i = models.data.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_update(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_quit(self, line):
        """Quit the console"""
        time.sleep(1)
        exit()

    def do_EOF(self, line):
        """Quit the console"""
        time.sleep(1)
        exit()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
