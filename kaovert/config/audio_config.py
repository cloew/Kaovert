from .flex import Config, FlexAttr, WrappedAttr

class AudioConfig(Config):
    """ Represents the Audio Config for a Conversion Configuration """
    includeAll = FlexAttr('includeAll')
    streams = WrappedAttr('streams', list)