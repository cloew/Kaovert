from .flex import FlexAttr, WrappedAttr

from kao_decorators import lazy_property
from kao_dict import KaoDict

class SubtitleConfig(KaoDict):
    """ Represents the Subtitle Configuration """
    includeAll = FlexAttr('includeAll')
    tracks = WrappedAttr('tracks', list)
    
    @lazy_property
    def tracksById(self):
        """ Return a dictionary fo track id to track """
        return {track.track:track for track in self.tracks}
    
    def find(self, trackToFind):
        """ Find the Subtitle that matches the given track """
        for track in self.tracks:
            if track.track == trackToFind:
                return track
        else:
            None