
class StopAt:
    """ Represents the Stop At CLI parameter """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.stopAt is not None
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        return ["--stop-at", context.config.stopAt]