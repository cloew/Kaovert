from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg

class SetPreset:
    """ Represents a command to create a Conversion Config file """
    description = "Set the preset in a config file"
    args = [Arg('preset', action='store', help='Preset to store'),
            ConversionConfigArg()]
        
    def run(self, *, preset, config):
        """ Run the command """
        config.preset = preset
        config.save()