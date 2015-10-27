from kao_command.args import FlagArg

class InlineArgs(FlagArg):
    """ Represents a CLI Argument for providing multiple inline arguments """
    
    def __init__(self):
        """ Initialize the Arg """
        FlagArg.__init__(self, '-a', '--args', action="store", nargs='+', help="Specify the additional args: arg=value")
    
    def getValue(self, args):
        """ Return the value from the args """
        inlineArgs = FlagArg.getValue(self, args)
        inlineArgs = [arg.split('=') for arg in inlineArgs]
        return {arg[0]:arg[1] for arg in inlineArgs}
        return ConversionConfig(filename)