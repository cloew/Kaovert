from .subtitle_track_config import SubtitleTrackConfig
from .flex import Config, FlexAttr, WrappedAttr, WrapperList

from kao_decorators import lazy_property

class SubtitleConfig(Config):
    """ Represents the Subtitle Configuration """
    includeAll = FlexAttr('includeAll')
    tracks = WrappedAttr('tracks', WrapperList, kwargs={'wrapperCls':SubtitleTrackConfig})
    
    @lazy_property
    def tracksById(self):
        """ Return a dictionary fo track id to track """
        return {track.id:track for track in self.tracks}
    
    def find(self, trackId):
        """ Find the Subtitle that matches the given track id """
        for track in self.tracks:
            if track.id == trackId:
                return track
        else:
            None