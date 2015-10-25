from .toml_attrs import toml_attrs

from kao_decorators import lazy_property, proxy_for
from kao_toml import KaoToml

@proxy_for('_toml', ['save'])
@toml_attrs('audio', 'output', 'stopAt')
class ConversionConfig:
    """ Represents a Conversion Configuration """
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)