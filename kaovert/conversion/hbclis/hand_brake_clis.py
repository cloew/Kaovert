from enum import Enum

from .output_location import OutputLocation

class HandBrakeClis(Enum):
    """ Represents the various potential command line arguments """
    OutputLocation = OutputLocation()
    
    def check(self, *args, **kwargs):
        """ Check if this CLI arg should be used """
        return self.value.check(*args, **kwargs)
    
    def build(self, *args, **kwargs):
        """ Build this CLI arg """
        return self.value.build(*args, **kwargs)