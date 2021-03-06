from ..mkv_wrapper import MkvWrapper
from kao_command.args import Arg

class ListSubtitleTracks:
    """ Represents a command to list the Subtitle Tracks for a file """
    description = "List Subtitle Tracks"
    args = [Arg('filename', action='store', help='MKV file to inspect')]
        
    def run(self, *, filename):
        """ Run the command """
        mkv = MkvWrapper.open(filename)
            
        for i, track in enumerate(mkv.subtitle_tracks):
            print("{0}: {1}, default={2}, forced={3}".format(i+1, track.language, track.default, track.forced))