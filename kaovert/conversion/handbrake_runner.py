from subprocess import call

class HandbrakeRunner:
    """ Helper class to manage running the HandBrakeCLI executable """
    
    def __init__(self):
        """ Initialize the Handbrake Runner """
        self.args = ['./HandBrakeCLI.exe']
        
    def addArgs(self, args):
        """ Add the arguments to the stored args """
        self.args.extend(args)
        
    def run(self):
        """ Run the command """
        print(" ".join(self.args))
        call(self.args)