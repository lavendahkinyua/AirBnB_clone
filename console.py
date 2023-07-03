"""
This module contains the command interpreter for the HBNB program.

The command interpreter provides a command line interface for interacting with the HBNB application.
"""
#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB program.

    This class extends the `cmd.Cmd` class and provides custom commands and prompt for the HBNB application.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit the command interpreter.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command interpreter.

        This command can be used by pressing Ctrl+D or entering 'EOF'.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

