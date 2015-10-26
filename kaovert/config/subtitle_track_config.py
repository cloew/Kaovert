from .flex import FlexAttr
from kao_dict import KaoDict

class SubtitleTrackConfig(KaoDict):
    """ Represents a Subtitle Track Configuration """
    id = FlexAttr('track')
    burn = FlexAttr('burn')