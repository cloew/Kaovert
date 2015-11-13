
class Video:
    """ Represents the video CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return len(context.config.video) > 0
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        video = context.config.video
        
        params = ["-e", video.encoder]
        if video.preset is not None:
            params.extend(['--encoder-preset', video.preset])
        return params