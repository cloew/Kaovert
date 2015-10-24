from kao_decorators import lazy_property
from kao_toml import KaoToml

@proxy_for('_toml', ['save'])
class ConversionConfig:
    """ Represents a Conversion Configuration """
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)