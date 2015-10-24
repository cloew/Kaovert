from kao_decorators import lazy_property, proxy_for
from kao_toml import KaoToml

CONFIG_ATTRS = {'output'}


@proxy_for('_toml', ['save'])
@proxy_for('_toml', CONFIG_ATTRS)
class ConversionConfig:
    """ Represents a Conversion Configuration """
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)