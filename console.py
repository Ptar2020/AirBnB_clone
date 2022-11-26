#!/usr/bin/python3
import cmd
import time
import sys
from models.base_model import BaseModel
"""The console class"""


class HBNBCommand(cmd.Cmd):
    """The HBNB main class"""
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel,
               #    'Amenity': Amenity,
               #    'State': State, 'Place': Place, 'Review': Review,
               #    'User': User, 'City': City
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
            else:
                print("**class doesn't exist**")
        return

    def do_show(self, line):
        pass

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
