from .toml_attrs import toml_attrs, toml_lists
from kao_decorators import lazy_property
from kao_dict import KaoDict

@toml_attrs('includeAll')
@toml_lists('tracks')
class SubtitleConfig(KaoDict):
    """ Represents the Subtitle Configuration """
    
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