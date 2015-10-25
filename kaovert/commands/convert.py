from ..config import ConversionConfig
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class Convert:
    """ Represents a command to create a Conversion Config file """
    description = "Convert a video file"
    args = [Arg('filenames', action='store', nargs='+', help='Files to convert'),
            FlagArg('-c', '--config', action='store', help="Config file to use for conversion")]
        
    def run(self, *, filenames, config):
        """ Run the command """
        config = ConversionConfig(config)
        converter = Converter(config)
        
        converter.run(filenames)