from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class Convert:
    """ Represents a command to create a Conversion Config file """
    description = "Convert a video file"
    args = [Arg('filenames', action='store', nargs='+', help='Files to convert'),
            ConversionConfigArg()]
        
    def run(self, *, filenames, config):
        """ Run the command """
        converter = Converter(config)
        converter.run(filenames)