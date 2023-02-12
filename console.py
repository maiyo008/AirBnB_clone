#!/usr/bin/python3
# console.py

"""Entry point for the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Inherits from the cmd module and defines methods to
    initialize commands for the interpreter"""

    prompt = "(hbnb)"
    class_dict = {"BaseModel": BaseModel}

    def do_EOF(self, line):
        """Exiting the program cleanly"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Empty line + ENTER should not execute anything
        """
        pass
    
    def do_create(self, name):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not name:
            print("**class name missing**")
        elif name != "BaseModel":
            print("**class doesn't exist**")
        else:
            my_model = BaseModel()
            my_model.save()
            instance_dict[my_model.id] = my_model
            print(my_model.id)
    
    def do_show(self, name):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(name)
        if not name:
            print("**class name missing")
        elif args[0] != "BaseModel":
            print("**class doesn't exist")
        elif len(args) == 1:
            print("**instance id missing**")
        else:
            keys = "{}.{}".format(args[0], args[1])
            if keys not in storage.all():
                print("**no instance found**")
            else:
                for key, value in storage.all().items():
                    if key == keys:
                        print(key, value)
                        break
    def do_destroy(self, name):
        """
        Deletes an instance based only on class name
        and id  (save it to the JSON file)
        """
        args = shlex.split(name)
        if not args:
            print("**class name missing**")
        elif args[0] != "BaseModel":
            print("**class doesn't exist**")
        elif len(args) == 1:
            print("**instance id is missing**")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("**no instance found**")
            else:
                del storage.all()[key]
                storage.save()
    def do_all(self, name):
        """
        Prints all the string representation of all 
        instances based on or not the class name
        """
        args = shlex.split(name)
        if len(args) == 1:
            class_name = args[0]
            if class_name not in HBNBCommand.class_dict:
                print("**class doesn't exist**")
            else:
                obj = storage.all()
            print([str(obj) for obj in obj.values()])
        else:
            obj = storage.all()
            print([str(obj) for obj in obj.values()])
    
    def do_update(self, name):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the chanfe into the JSON file)
        """
        args = shlex.split(name)
        if not args:
            print("**class name missing**")
        elif len(args) == 1:
            class_name = args[0]
            if class_name not in HBNBCommand.class_dict:
                print("**class doesn't exist**")
            else:
                print("**instance id missing**")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("**no instance found")
            else:
                print("**attribute name missing**")
        elif len(args) == 3:
            print("**value missing**")
        elif len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            attr_name = args[2]
            attr_value = args[3]
            if attr_name != "id" or attr_name != "created_at" or attr_name != "updated_at":
                setattr(storage.all()[key], attr_name, attr_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
