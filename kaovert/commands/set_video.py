from ..args import ConversionConfigArg

from kao_command.args import Arg

class SetVideo:
    """ Represents a command to set the video settings for a Conversion Config file """
    description = "Set the Video Settings in a config file"
    args = [Arg('encoder', action='store', help='Encoder to store'),
            ConversionConfigArg()]
        
    def run(self, *, encoder, config):
        """ Run the command """
        config.video.encoder = encoder
        config.save()