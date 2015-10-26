from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg

class AddSubtitle:
    """ Represents a command to create a Conversion Config file """
    description = "Add a subtitle track to a config file"
    args = [Arg('track', action='store', help='Track # to add to the config (1 for the first stream, scan for Foreign Audio)'),
            ConversionConfigArg()]
        
    def run(self, *, track, config):
        """ Run the command """
        if track == 'all':
            config.subtitle.includeAll = True
        else:
            config.subtitle.tracks.append({'track':track})
        config.save()