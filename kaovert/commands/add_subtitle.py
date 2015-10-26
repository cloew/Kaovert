from ..args import ConversionConfigArg
from ..config import SubtitleTrackConfig
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class AddSubtitle:
    """ Represents a command to create a Conversion Config file """
    description = "Add a subtitle track to a config file"
    args = [Arg('track', action='store', help='Track # to add to the config (1 for the first stream, scan for Foreign Audio)'),
            ConversionConfigArg(),
            FlagArg('-b', '--burn', action='store_true', help="Flag the track to be burned into the picture"),
            FlagArg('-d', '--default', action='store_true', help="Flag the track as the default track"),
            FlagArg('-f', '--forced', action='store_true', help="Flag the track to be forced")]
        
    def run(self, *, track, config, burn, default, forced):
        """ Run the command """
        if track == 'all':
            config.subtitle.includeAll = True
        else:
            subtitleTrack = config.subtitle.find(track)
            if not subtitleTrack:
                subtitleTrack = SubtitleTrackConfig(id=track)
                config.subtitle.tracks.append(subtitleTrack)
                
            if burn:
                subtitleTrack.burn = True
            if default:
                subtitleTrack.default = True
            if forced:
                subtitleTrack.forced = True
                
        config.save()