from ..config import ConversionConfig
from kao_command.args import Arg, FlagArg

class NewConfig:
    """ Represents a command to create a Conversion Config file """
    description = "Create Conversion Config file"
    args = [Arg('filename', action='store', help='Config file to create'),
            FlagArg('-o', '--output', action='store', help="Output file location")]
        
    def run(self, *, filename, output):
        """ Run the command """
        with open(filename, 'w') as f:
            pass
            
        config = ConversionConfig(filename)
        
        if output is not None:
            print('Setting output:', output)
            config.output = output
        config.save()
        