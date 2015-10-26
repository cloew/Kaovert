
class Audio:
    """ Represents the audio CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.audio is not None and len(context.config.audio) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        audio = context.config.audio
        if audio.includeAll:
            streams = [str(i+1) for i, stream in enumerate(context.mkv.audio_tracks)]
        else:
            streams = [str(stream.number) for stream in context.config.audio.streams]
        return ["-a", ",".join(streams)]