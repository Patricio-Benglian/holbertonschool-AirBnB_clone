#!/usr/bin/python3
"""
content module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Does commands i guess """
    prompt = "(hbnb) "

    def do_quit(self, input):
        """ quit """
        quit()

    def do_EOF(self, input):
        """ quits """
        print()
        quit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()