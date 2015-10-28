from ..args import ConversionConfigArg, InlineArgs
from ..conversion import HandbrakeRunner

from kao_command.args import Arg, FlagArg

class ListPresets:
    """ Represents a command to list the available presets """
    description = "List Handbrake Presets"
    args = []
        
    def run(self):
        """ Run the command """
        runner = HandbrakeRunner()
        runner.addArgs(['-z'])
        runner.run()