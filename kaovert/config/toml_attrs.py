from kao_dict import KaoDict

def toml_attrs(*attrs):
    """ Add properties for the attrs to provide an interface based on the contents of TOML file """
    def addAttrData(cls):
        def add_property(cls, attr):
            def setter(self, v):
                setattr(self._toml, attr, v)
            def getter(self):
                return getattr(self._toml, attr) if attr in self._toml else None
            setattr(cls, attr, property(getter, setter))
            
        for attr in attrs:
            add_property(cls, attr)
        return cls
    return addAttrData
    
def toml_group(*groups):
    """ Add properties for the groups to provide an interface based on the contents of TOML file """
    def addGroupData(cls):
        def add_property(cls, group):
            def setter(self, v):
                setattr(self._toml, group, v)
            def getter(self):
                if group not in self._toml:
                    setattr(self._toml, group, KaoDict())
                return getattr(self._toml, group)
            setattr(cls, group, property(getter, setter))
            
        for group in groups:
            add_property(cls, group)
        return cls
    return addGroupData