from .audio_stream_config import AudioStreamConfig
from flexconfig import Config, FlexAttr, WrappedAttr, WrapperList

class AudioConfig(Config):
    """ Represents the Audio Config for a Conversion Configuration """
    includeAll = FlexAttr('includeAll')
    streams = WrappedAttr('streams', WrapperList, kwargs={'wrapperCls':AudioStreamConfig})