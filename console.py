#!/usr/bin/python3
"""
content module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Does commands i guess """
    prompt = "(hbnb) "

    def do_quit(self, input):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, input):
        """Quit command to exit the program"""
        print()
        quit()

    def do_create(self, input):
        """placeholder"""
        pass

    def do_show(self, input):
        """placeholder"""
        pass

    def do_pass(self, input, id):
        """placeholder"""
        pass

    def do_destroy(self, input, id):
        """placeholder"""
        pass

    def do_all(self, input):
        """placeholder"""
        pass

    def do_update(self, input, id, attr_name, attr_val):
        """placeholder"""
        pass

    def emptyline(self):
        """ Does nothing """
        # Actually pass though, not placeholder
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
