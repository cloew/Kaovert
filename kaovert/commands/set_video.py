from ..args import ConversionConfigArg

from kao_command.args import Arg, FlagArg

class SetVideo:
    """ Represents a command to set the video settings for a Conversion Config file """
    description = "Set the Video Settings in a config file"
    args = [Arg('encoder', action='store', help='Encoder to store'),
            ConversionConfigArg(),
            FlagArg('-p', '--preset', action='store', help="The encoder preset")]
        
    def run(self, *, encoder, config, preset):
        """ Run the command """
        config.video.encoder = encoder
        if preset:
            config.video.preset = preset
        config.save()