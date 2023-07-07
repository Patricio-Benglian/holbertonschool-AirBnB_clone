#!/usr/bin/python3
"""
content module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Does commands i guess """
    prompt = "(hbnb) "
    acceptableClasses = {
        "BaseModel"
    }

    def verifyArgs(self, args, doupdate=False):
        """verifies Class and Instance ID"""
        try:
            className = args[0]
        except Exception:
            print("** class name missing **")
            return False
        if className not in HBNBCommand.acceptableClasses:
            print("** class doesn't exist **")
            return False
        try:
            instanceID = args[1]
        except Exception:
            print("** instance id missing **")
            return False
        key = f"{className}.{instanceID}"
        if key not in storage.all():
            print("** no instance found **")
            return False
        if doupdate:
            try:
                attrName = args[2]
            except Exception:
                print("** attribute name missing **")
                return False
            try:
                attrValue = args[3]
            except Exception:
                print("** value missing **")
                return False
        return True


    def split(self, string):
        list = string.split()
        return list

    def do_quit(self, input):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, input):
        """Quit command to exit the program"""
        print()
        quit()

    def do_create(self, input):
        """creates instance of BaseModel"""
        if input is None:
            print ("** class name missing **")
        elif input not in HBNBCommand.acceptableClasses:
            print("** class doesn't exist **")
        instance = eval(input + "()")
        storage.new(instance)
        storage.save()
        print (instance.id)


    def do_show(self, input):
        """prints str representation of instance"""
        args = self.split(input)
        if not self.verifyArgs(args):
            return
        className = args[0]
        instanceID = args[1]
        key = f"{className}.{instanceID}"
        print (storage.all()[key])

    def do_destroy(self, input):
        """Deletes an instance"""
        args = self.split(input)
        if not self.verifyArgs(args):
            return
        className = args[0]
        instanceID = args[1]
        key = f"{className}.{instanceID}"
        del storage.all()[key]
        storage.save()

    def do_all(self, input):
        """placeholder"""
        if input:
            if input not in HBNBCommand.acceptableClasses:
                print("** class doesn't exist **")
                return
            for object in storage.all():
                if object.__class__ == input:
                    print(storage.all()[object], sep="")
        for object in storage.all():
            print(storage.all()[object], sep="")

    def do_update(self, input):
        """updates attribute of an instance"""
        args = self.split(input)
        if not self.verifyArgs(args, doupdate=True):
            return
        className = args[0]
        instanceID = args[1]
        attrName = args[2]
        attrValue = args[3]
        key = f"{className}.{instanceID}"
        # Cringe fix because it passes string quotes as string
        if attrValue[0] == '"' and attrValue[-1] == '"':
            attrValue = attrValue[1:-1]
        setattr(storage.all()[key], attrName, attrValue)
        storage.save()

    def emptyline(self):
        """ Does nothing """
        # Actually pass though, not placeholder
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
