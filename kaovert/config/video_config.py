from .audio_stream_config import AudioStreamConfig

from flexconfig import Config, FlexAttr, WrappedAttr, WrapperList
from kao_decorators import lazy_property
from kao_listdict import ListDict

class VideoConfig(Config):
    """ Represents the Video Config for a Conversion Configuration """
    encoder = FlexAttr('encoder')