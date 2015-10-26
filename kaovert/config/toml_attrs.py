from kao_dict import KaoDict

class PropertyAdder:
    
    def __init__(self, attrs, toml, default=None):
        self.attrs = attrs
        self.toml = toml
        self.default = default
        
    def add(self, cls):
        """ Add the property to the cls """
        toml = self.toml
        default = self.default
        def addProperty(cls, attr):
            def setter(self, v):
                setattr(gettoml(self, toml), attr, v)
                
            if default is None:
                def getter(self):
                    tomlDict = gettoml(self, toml)
                    return tomlDict[attr] if attr in tomlDict else None
            else:
                def getter(self):
                    tomlDict = gettoml(self, toml)
                    if attr not in tomlDict:
                        setattr(tomlDict, attr, default())
                    value = tomlDict[attr]
                    if type(value) is not default:
                        setattr(tomlDict, attr, default(value))
                    return tomlDict[attr]
            setattr(cls, attr, property(getter, setter))
        
        for attr in self.attrs:
            addProperty(cls, attr)
        return cls
        

def gettoml(self, toml):
    return self if toml is None else getattr(self, toml)
    
def toml_attrs(*attrs, toml=None):
    """ Add properties for the attrs to provide an interface based on the contents of TOML file """
    propsAdder = PropertyAdder(attrs, toml)
    return propsAdder.add
    
def toml_config(*attrs, toml=None, config=None):
    """ Add properties for the config wrappers to provide an interface based on the contents of the underlying TOML dictionary """
    propsAdder = PropertyAdder(attrs, toml, default=config)
    return propsAdder.add
    
def toml_lists(*attrs, toml=None):
    """ Add properties for the attributes from the Toml File that should be lists """
    propsAdder = PropertyAdder(attrs, toml, default=list)
    return propsAdder.add