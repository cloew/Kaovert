from ..mkv_wrapper import MkvWrapper
from kao_command.args import Arg

class ListAudioTracks:
    """ Represents a command to list the Audio Tracks for a file """
    description = "List Audio Tracks"
    args = [Arg('filename', action='store', help='MKV file to inspect')]
        
    def run(self, *, filename):
        """ Run the command """
        mkv = MkvWrapper.open(filename)
            
        for i, track in enumerate(mkv.audio_tracks):
            print("{0}: {1}".format(i+1, track.language))