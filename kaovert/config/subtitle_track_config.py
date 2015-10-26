from .flex import Config, FlexAttr

class SubtitleTrackConfig(Config):
    """ Represents a Subtitle Track Configuration """
    id = FlexAttr('track')
    burn = FlexAttr('burn')
    forced = FlexAttr('forced')