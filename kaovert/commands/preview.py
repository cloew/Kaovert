from ..args import ConversionConfigArg
from ..conversion import Converter

from kao_command.args import Arg, FlagArg

class Preview:
    """ Represents a command to create a Conversion Config file """
    description = "Create a Preview Conversion of a video file"
    args = [Arg('filenames', action='store', nargs='+', help='Files to preview'),
            ConversionConfigArg(),
            FlagArg('-s', '--start', action='store', type=int, default=0, help="Specify the start time for the preview"),
            FlagArg('-d', '--duration', action='store', type=int, default=30, help="Specify the duration to stop at")]
        
    def run(self, *, filenames, config, start, duration):
        """ Run the command """
        config.startAt = "duration:{0}".format(start)
        config.stopAt = "duration:{0}".format(duration)
        converter = Converter(config)
        converter.run(filenames)