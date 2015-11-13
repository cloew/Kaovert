from ..args import ConversionConfigArg
from ..config import AudioStreamConfig
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class AddAudio:
    """ Represents a command to create a Conversion Config file """
    description = "Add a audio stream to a config file"
    args = [Arg('stream', action='store', help='Stream # to add to the config (1 for the first stream)'),
            ConversionConfigArg(),
            FlagArg('-e', '--encoder', action='store', help="The encoder to use for the Audio Stream"),
            FlagArg('-m', '--mixdown', action='store', help="The mixdown format to use for the Audio Stream"),
            FlagArg('-d', '--drc', action='store', help="The Dynamic Range Compression value to use for the Audio Stream"),
            FlagArg('-g', '--gain', action='store', help="The Decibel Gain value")]
        
    def run(self, *, stream, config, encoder, mixdown, drc, gain):
        """ Run the command """
        if stream == 'all':
            config.audio.includeAll = True
        else:
            audioStream = AudioStreamConfig(number=stream)
            config.audio.streams.append(audioStream)
            
            if encoder:
                audioStream.encoder = encoder
            if mixdown:
                audioStream.mixdown = mixdown
            if drc:
                audioStream.drc = drc
            if gain:
                audioStream.gain = gain
        config.save()