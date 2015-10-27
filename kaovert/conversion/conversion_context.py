from ..mkv_wrapper import MkvWrapper
from kao_decorators import lazy_property

class ConversionContext:
    """ Represents the context for a file's conversion """
    
    def __init__(self, filename, config, args):
        """ Initialize with the filename and config for the conversion """
        self.filename = filename
        self.config = config
        self.args = args
        
    @lazy_property
    def mkv(self):
        """ Return the MKV wrapper """
        return MkvWrapper.open(self.filename)