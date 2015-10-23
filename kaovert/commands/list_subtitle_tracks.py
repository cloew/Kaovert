from kao_command.args import Arg
import enzyme

class ListSubtitleTracks:
    """ Represents a command to list the Subtitle Tracks for a file """
    description = "List Subtitle Tracks"
    args = [Arg('filename', action='store', help='MKV file to inspect')]
        
    def run(self, *, filename):
        """ Run the command """
        with open(filename, 'rb') as f:
            mkv = enzyme.MKV(f)
            
        for i, track in enumerate(mkv.subtitle_tracks):
            print("{0}: {1}".format(i+1, track.language))