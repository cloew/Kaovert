from .conversion_args import ConversionArgs
from .conversion_context import ConversionContext
from .handbrake_runner import HandbrakeRunner
from .hbclis import HandBrakeClis

from glob import glob
import os

class Converter:
    """ Represents a Converter than can convert files using the HandBrakeCLI """
    
    def __init__(self, config):
        """ Initialize with the config """
        self.config = config
        
    def run(self, paths, **kwargs):
        """ Run the Converter for the given filenames """
        filenames = self.getFilenames(paths)
        
        for i, filename in enumerate(filenames):
            runner = HandbrakeRunner()
            runner.addArgs(['-i', filename])
            
            conversionArgs = ConversionArgs(filename, i, **kwargs)
            context = ConversionContext(filename, self.config, conversionArgs)
            
            for cliArg in HandBrakeClis:
                if cliArg.check(context):
                    runner.addArgs(cliArg.build(context))
                    
            runner.run()
            
    def getFilenames(self, paths):
        """ Return the proper filenames """
        filenames = []
        for path in paths:
            if os.path.isdir(path):
                filenames.extend(glob(os.path.join(path, '*.mkv')))
            else:
                filenames.append(path)
        return filenames