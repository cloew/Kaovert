from ..args import ConversionConfigArg
from ..config import AudioStreamConfig
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class AddAudio:
    """ Represents a command to create a Conversion Config file """
    description = "Add a audio stream to a config file"
    args = [Arg('stream', action='store', help='Stream # to add to the config (1 for the first stream)'),
            ConversionConfigArg(),
            FlagArg('-e', '--encoder', action='store', help="The encoder to use for the Audio Stream")]
        
    def run(self, *, stream, config, encoder):
        """ Run the command """
        if stream == 'all':
            config.audio.includeAll = True
        else:
            audioStream = AudioStreamConfig(number=stream)
            config.audio.streams.append(audioStream)
            
            if encoder:
                audioStream.encoder = encoder
        config.save()