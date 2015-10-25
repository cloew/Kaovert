from subprocess import call
import os

class Converter:
    """ Represents a Converter than can convert files using the HandBrakeCLI """
    
    def __init__(self, config):
        """ Initialize with the config """
        self.config = config
        
    def run(self, filenames):
        """ Run the Converter for the given filenames """
        for filename in filenames:
            call(['./HandBrakeCLI.exe', '-i', filename, '-o', self.getOutput(filename)])
            
    def getOutput(self, filename):
        """ Return the proper output filename """
        output = self.config.output
        if output is None:
            output = filename
            output = self.config.output
        elif os.path.isdir(output):
            output = os.path.join(output, filename)
        return output