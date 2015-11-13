from flexconfig import Config, FlexAttr

class AudioStreamConfig(Config):
    """ Represents an Audio Stream Configuration """
    number = FlexAttr('number')
    encoder = FlexAttr('encoder', default='copy')
    mixdown = FlexAttr('mixdown', default='')
    drc = FlexAttr('drc', default='')