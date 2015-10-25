
class ConversionContext:
    """ Represents the context for a file's conversion """
    
    def __init__(self, filename, config):
        """ Initialize with the filename and config for the conversion """
        self.filename = filename
        self.config = config