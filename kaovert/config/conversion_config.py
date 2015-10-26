from .audio_config import AudioConfig
from .subtitle_config import SubtitleConfig
from .toml_attrs import toml_attrs, toml_config

from kao_decorators import lazy_property, proxy_for
from kao_toml import KaoToml

@proxy_for('_toml', ['save'])
@toml_attrs('output', 'stopAt', toml='_toml')
@toml_config('audio', config=AudioConfig, toml='_toml')
@toml_config('subtitle', config=SubtitleConfig, toml='_toml')
class ConversionConfig:
    """ Represents a Conversion Configuration """
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)