
class Subtitles:
    """ Represents the subtitle CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.subtitle is not None and len(context.config.subtitle) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        subtitle = context.config.subtitle
        if subtitle.includeAll:
            tracks = [str(i+1) for i, track in enumerate(context.mkv.subtitle_tracks)]
            tracks.append('scan')
        else:
            tracks = [str(track.track) for track in context.config.subtitle.tracks]
        return ["-s", ",".join(tracks)]