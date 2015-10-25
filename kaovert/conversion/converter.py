from .conversion_context import ConversionContext
from .hbclis import HandBrakeClis

from subprocess import call

class Converter:
    """ Represents a Converter than can convert files using the HandBrakeCLI """
    
    def __init__(self, config):
        """ Initialize with the config """
        self.config = config
        
    def run(self, filenames):
        """ Run the Converter for the given filenames """
        for filename in filenames:
            args = ['./HandBrakeCLI.exe', '-i', filename]
            context = ConversionContext(filename, self.config)
            for cliArg in HandBrakeClis:
                if cliArg.check(context):
                    args.extend(cliArg.build(context))
                    
            print(" ".join(args))
            call(args)
            