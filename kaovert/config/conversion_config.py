from .audio_config import AudioConfig
from .subtitle_config import SubtitleConfig

from flexconfig import ConfigPath, FlexAttr, WrappedAttr
from kao_decorators import lazy_property, proxy_for
from kao_toml import KaoToml

@proxy_for('_toml', ['save'])
class ConversionConfig:
    """ Represents a Conversion Configuration """
    _output = FlexAttr('output', data='_toml')
    output = ConfigPath('_output')
    preset = FlexAttr('preset', data='_toml')
    startAt = FlexAttr('startAt', data='_toml')
    stopAt = FlexAttr('stopAt', data='_toml')
    audio = WrappedAttr('audio', AudioConfig, data='_toml')
    subtitle = WrappedAttr('subtitle', SubtitleConfig, data='_toml')
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)