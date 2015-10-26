from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg, FlagArg
from kao_dict import KaoDict

class AddSubtitle:
    """ Represents a command to create a Conversion Config file """
    description = "Add a subtitle track to a config file"
    args = [Arg('track', action='store', help='Track # to add to the config (1 for the first stream, scan for Foreign Audio)'),
            ConversionConfigArg(),
            FlagArg('-b', '--burn', action='store_true', help="Flag the track to be burned into the picture")]
        
    def run(self, *, track, config, burn):
        """ Run the command """
        if track == 'all':
            config.subtitle.includeAll = True
        else:
            subtitleTrack = config.subtitle.find(track)
            if not subtitleTrack:
                subtitleTrack = KaoDict({'track':track})
                config.subtitle.tracks.append(subtitleTrack)
                
            if burn:
                subtitleTrack.burn = True
                
        config.save()