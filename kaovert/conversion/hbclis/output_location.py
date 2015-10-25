import os

class OutputLocation:
    """ Represents the Output Location CLI parameter """
    
    def check(self, filename, config):
        """ Return if this CLI should be used """
        return True
        
    def build(self, filename, config):
        """ Return the string parameters to add to the command string """
        output = self.getOutput(filename, config)
        return ["-o", output]
        
    def getOutput(self, filename, config):
        """ Return the proper output filename """
        output = config.output
        if output is None:
            output = filename
        elif os.path.isdir(output):
            output = os.path.join(output, filename)
        return output