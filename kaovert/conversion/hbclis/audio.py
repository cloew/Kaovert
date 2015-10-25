
class Audio:
    """ Represents the audio CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.audio is not None and len(context.config.audio) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        streams = [stream for stream in context.config.audio if stream.isdigit()]
        return ["-a", ",".join(streams)]