from kao_decorators import proxy_for
import enzyme

@proxy_for('mkv', ['audio_tracks', 'subtitle_tracks'])
class MkvWrapper:
    """ Helper class to wrap MKV Files """
    
    @classmethod
    def open(cls, filename):
        """ Open the file as a MKV file """
        with open(filename, 'rb') as f:
            file = cls(f)
        return file
    
    def __init__(self, file):
        """ Initialize with the file to wrap """
        self.mkv = enzyme.MKV(file)