from kao_decorators import lazy_property, proxy_for
from kao_toml import KaoToml

@proxy_for('_toml', ['save'])
class ConversionConfig:
    """ Represents a Conversion Configuration """
    
    def __init__(self, filename):
        """ Initialize the Conversion Config """
        self.filename = filename
        
    @property
    def output(self):
        """ Return the output if it is specified in the TOML file """
        return self._toml.output if 'output' in self._toml else None
        
    @property
    def stopAt(self):
        """ Return the stopAt if it is specified in the TOML file """
        return self._toml.stopAt if 'stopAt' in self._toml else None
        
    @lazy_property
    def _toml(self):
        """ Return the Toml file """
        return KaoToml(self.filename)