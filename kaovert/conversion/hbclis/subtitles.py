
class Subtitles:
    """ Represents the subtitle CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.subtitle is not None and len(context.config.subtitle) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        subtitle = context.config.subtitle
        trackIds = self.getTrackIds(context)
        
        burnIndex = None
        
        for i, trackId in enumerate(trackIds):
            print(trackId in subtitle.tracksById)
            if trackId in subtitle.tracksById:
                track = subtitle.tracksById[trackId]
                if track.burn:
                    burnIndex = i+1
            
        params = ["-s", ",".join(trackIds)]
        if burnIndex is not None:
            params.extend(['--subtitle-burn', str(burnIndex)])
        return params
        
    def getTrackIds(self, context):
        """ REturn the selected track ids """
        subtitle = context.config.subtitle
        if subtitle.includeAll:
            trackIds = [str(i+1) for i, track in enumerate(context.mkv.subtitle_tracks)]
            trackIds.append('scan')
        else:
            trackIds = [str(track.track) for track in context.config.subtitle.tracks]
        return trackIds