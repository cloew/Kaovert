from .conversion_args import ConversionArgs
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
        for i, filename in enumerate(filenames):
            conversionArgs = ConversionArgs(filename, i)
            context = ConversionContext(filename, self.config, conversionArgs)
            
            cliArgs = ['./HandBrakeCLI.exe', '-i', filename]
            for cliArg in HandBrakeClis:
                if cliArg.check(context):
                    cliArgs.extend(cliArg.build(context))
                    
            call(cliArgs)
            