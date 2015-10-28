
class Preset:
    """ Represents the subtitle CLI parameters """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return context.config.preset is not None
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        return ['-Z', context.config.preset]