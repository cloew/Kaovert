from ..config import ConversionConfig
from kao_command.args import Arg

class NewConfig:
    """ Represents a command to create a Conversion Config file """
    description = "Create Conversion Config file"
    args = [Arg('filename', action='store', help='Config file to create')]
        
    def run(self, *, filename):
        """ Run the command """
        with open(filename, 'w') as f:
            pass
            
        config = ConversionConfig(filename)
        config.output = "Some Output file"
        config.save()