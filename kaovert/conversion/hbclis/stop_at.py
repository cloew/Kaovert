
class StopAt:
    """ Represents the Stop At CLI parameter """
    
    def check(self, filename, config):
        """ Return if this CLI should be used """
        return config.stopAt is not None
        
    def build(self, filename, config):
        """ Return the string parameters to add to the command string """
        return ["--stop-at", config.stopAt]