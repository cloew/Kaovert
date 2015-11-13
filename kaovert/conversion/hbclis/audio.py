from .audio_stream_accessor import AudioStreamAccessor
from .list_arg import ListArg

class Audio:
    """ Represents the audio CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.audio is not None and len(context.config.audio) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        audio = context.config.audio
        streamNumbers = self.getStreamNumbers(context)
        streamAccesor = AudioStreamAccessor(audio)
        
        encoders = ListArg()
        mixdown = ListArg()
        drc = ListArg()
        for number in streamNumbers:
            stream = streamAccesor[number]
            encoders.append(stream.encoder)
            mixdown.append(stream.mixdown)
            drc.append(stream.drc)
        
        return ["-a", streamNumbers.build(), '-E', encoders.build(), '-6', mixdown.build(), '-D', drc.build()]
        
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
        return ListArg(streams)
        
    def getExtraStreams(self, streams, configuredStreams):
        """ Return the Streams that are added as extras to the Audio Config """
        extraStreams = list(configuredStreams)
        for number in streams:
            if number in extraStreams:
                extraStreams.remove(number)
        return extraStreams