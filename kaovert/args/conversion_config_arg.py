from ..config import ConversionConfig
from kao_command.args import FlagArg

class ConversionConfigArg(FlagArg):
    """ Represents a CLI Argument that specifies a Conversion Config """
    
    def __init__(self):
        """ Initialize the Arg """
        FlagArg.__init__(self, '-c', '--config', action="store", help="Config file to use for conversion")
    
    def getValue(self, args):
        """ Return the value from the args """
        filename = FlagArg.getValue(self, args)
        return ConversionConfig(filename)