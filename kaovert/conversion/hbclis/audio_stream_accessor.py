from kaovert.config import AudioStreamConfig

class AudioStreamAccessor:
    """ Helper class to facilitate accessing the proper stream config """
    
    def __init__(self, audio):
        """ Initialize with the Audio Config """
        self.audio = audio
        self.timesRequested = {} # Tracks how many times a stream number has been requested
        
    def __getitem__(self, number):
        """ Return the stream config for the requested number """
        if number in self.audio.streamsByNumber:
            index = self.getStreamIndex(number)
            self.timesRequested[number] += 1
            return self.audio.streamsByNumber[number][index]
        else:
            return AudioStreamConfig(number=number)
        
    def getStreamIndex(self, number):
        """ Return the proper stream index based on how many times this number has been requested """
        if number not in self.timesRequested:
            self.timesRequested[number] = 0
        return self.timesRequested[number]