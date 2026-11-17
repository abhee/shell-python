import os, sys
from collections.abc import Callable
import fileutil


# Map containing bultins and their associated functions
_BUILTINS = {}

def is_builtin(name: str) -> bool:
    """Returns True if arg is a builtin, False otherwise"""
    return name in _BUILTINS

def get_builtin(name: str) -> Callable | None:
    """Return function object for name"""
    return _BUILTINS.get(name, None)

def builtin(name: str) -> Callable:
    """Decorator that maps builtin names to their functions."""
    def add(func):
        _BUILTINS[name] = func
        return func
    return add

@builtin("exit")
def _exit(args: list[str]) -> None:
    """exit: exits from the shell REPL."""
    sys.exit(int(args[0]) if (args and args[0].isdecimal())  else 0)

@builtin("echo")
def _echo(args: list[str]) -> None:
    """echo: prints all of its args to stdout."""
    print(" ".join(*args))

@builtin("pwd")
def _pwd(args: list[str]) -> None:
    """pwd: prints path of current working directory to stdout."""
    print(os.getcwd())
    
@builtin("type")
def _type(args: list[str]) -> None:
    """type: prints type of its argument."""
    for arg in args:
        # Handle bultins
        if is_builtin(arg):
            print(f"{arg} is a shell builtin")
        # Check whether arg is in path and is an executable
        elif (file_path := fileutil.find_exe_file(arg)) is not None:
            print(f"{arg} is {file_path}")
        else:
            # cmd is neither a bultin, nor an executable file
            print(f"{arg}: not found")

@builtin("cd")
def _cd(args: list[str]) -> None:
    """cd: changes working directory"""
    pass
