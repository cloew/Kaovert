from jinja2 import Template
import os

class OutputLocation:
    """ Represents the Output Location CLI parameter """
    
    def check(self, context):
        """ Return if this CLI should be used """
        return True
        
    def build(self, context):
        """ Return the string parameters to add to the command string """
        output = self.getOutput(context)
        return ["-o", output]
        
    def getOutput(self, context):
        """ Return the proper output filename """
        output = context.config.output
            
        if output is None:
            output = context.filename
        else:
            output = Template(output).render(**context.args)
            if os.path.isdir(output):
                output = os.path.join(output, context.filename)
        print(output)
        return output