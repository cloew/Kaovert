
class Audio:
    """ Represents the audio CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.audio is not None and len(context.config.audio) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        audio = context.config.audio
        streamNumbers = self.getStreamNumbers(context)
        
        return ["-a", ",".join(streamNumbers)]
        
    def getStreamNumbers(self, context):
        """ Return the selected Audio Stream Numbers """
        audio = context.config.audio
        configuredStreams = [str(stream.number) for stream in audio.streams]
        if audio.includeAll:
            streams = [str(i+1) for i, stream in enumerate(context.mkv.audio_tracks)]
            extraStreams = self.getExtraStreams(streams, configuredStreams)
            streams.extend(extraStreams)
        else:
            streams = configuredStreams
        return streams
        
    def getExtraStreams(self, streams, configuredStreams):
        """ Return the Streams that are added as extras to the Audio Config """
        extraStreams = list(configuredStreams)
        for number in streams:
            if number in extraStreams:
                extraStreams.remove(number)
        return extraStreams