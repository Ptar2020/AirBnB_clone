#!/usr/bin/python3
"""The console class"""
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

    def do_all(self, line):
        """ Method to print all instances """
        if len(line) == 0:
            print([str(a) for a in models.data.all().values()])
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in models.data.all().items() if line in b])

    def do_update(self, line):
        """ Method to update the JSON file"""
        line = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return
        elif line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print('** instance id missing **')
            return
        else:
            key = line[0] + '.' + line[1]
            if key in models.data.all():
                if len(line) > 2:
                    if len(line) == 3:
                        print('** value missing **')
                    else:
                        setattr(models.data.all()[key], line[2], line[3][1:-1])
                        models.data.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

    def precmd(self, line):
        """ This is executed just before the typed command is interpreted """
        args = line.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return line

    def do_destroy(self, line):
        """ Method to delete instance with class and id """
        if len(line) == 0:
            print("** class name missing **")
            return
        arg_list = line.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in models.data.all():
                models.data.all().pop(key)
                models.data.save()
            else:
                print('** no instance found **')
                return

    def do_count(self, line):
        """  retrieves the number of instances of a class """
        class_token = line.split()
        data = models.data.all()
        instances = 0
        if class_token[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in data:
                className = key.split('.')
                if className[0] == class_token[0]:
                    instances = instances + 1
            print(instances)

    def do_quit(self, line):
        """Quit the console"""
        time.sleep(1)
        exit()

    def do_EOF(self, line):
        """Quit the console"""
        time.sleep(1)
        exit()

    def emptyline(self):
        """ What happens when empty line is passed """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
