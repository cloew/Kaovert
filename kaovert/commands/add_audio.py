from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg

class AddAudio:
    """ Represents a command to create a Conversion Config file """
    description = "Add a audio stream to a config file"
    args = [Arg('stream', action='store', help='Stream # to add to the config (1 for the first stream)'),
            ConversionConfigArg()]
        
    def run(self, *, stream, config):
        """ Run the command """
        config.audio.streams.append({'number':stream})
        config.save()