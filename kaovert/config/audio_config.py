from .audio_stream_config import AudioStreamConfig

from flexconfig import Config, FlexAttr, WrappedAttr, WrapperList
from kao_decorators import lazy_property
from kao_listdict import ListDict

class AudioConfig(Config):
    """ Represents the Audio Config for a Conversion Configuration """
    includeAll = FlexAttr('includeAll')
    streams = WrappedAttr('streams', WrapperList, kwargs={'wrapperCls':AudioStreamConfig})
    
    @lazy_property
    def streamsByNumber(self):
        """ Return a dictionary of stream number to Streams """
        d = ListDict()
        for stream in self.streams:
            d[stream.number] = stream
        return d