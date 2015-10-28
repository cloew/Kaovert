from enum import Enum

from .audio import Audio
from .output_location import OutputLocation
from .preset import Preset
from .start_at import StartAt
from .stop_at import StopAt
from .subtitles import Subtitles

class HandBrakeClis(Enum):
    """ Represents the various potential command line arguments """
    Audio = Audio()
    OutputLocation = OutputLocation()
    Preset = Preset()
    StartAt = StartAt()
    StopAt = StopAt()
    Subtitles = Subtitles()
    
    def check(self, context):
        """ Check if this CLI arg should be used """
        return self.value.check(context)
    
    def build(self, context):
        """ Build this CLI arg """
        return self.value.build(context)