from .commands import commands
from kao_command import Driver

def Kaovert(scriptName):
    return Driver(scriptName, commands)