from .flex import FlexAttr, WrappedAttr
from kao_dict import KaoDict

class AudioConfig(KaoDict):
    """ Represents the Audio Config for a Conversion Configuration """
    includeAll = FlexAttr('includeAll')
    streams = WrappedAttr('streams', list)