from flexconfig import Config, FlexAttr

class SubtitleTrackConfig(Config):
    """ Represents a Subtitle Track Configuration """
    id = FlexAttr('track')
    burn = FlexAttr('burn')
    default = FlexAttr('default')
    forced = FlexAttr('forced')