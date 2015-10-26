
class StartAt:
    """ Represents the Start At CLI parameter """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.startAt is not None
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        return ["--start-at", context.config.startAt]