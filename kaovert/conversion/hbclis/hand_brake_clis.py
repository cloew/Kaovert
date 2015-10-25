from enum import Enum

from .output_location import OutputLocation
from .stop_at import StopAt

class HandBrakeClis(Enum):
    """ Represents the various potential command line arguments """
    OutputLocation = OutputLocation()
    StopAt = StopAt()
    
    def check(self, context):
        """ Check if this CLI arg should be used """
        return self.value.check(context)
    
    def build(self, context):
        """ Build this CLI arg """
        return self.value.build(context)