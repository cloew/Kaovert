from .get_data import getdata
from .kao_descriptor import KaoDescriptor

class WrappedAttr(KaoDescriptor):
    """ Represents an attribute that should be wrapped in a class before being returned """
    
    def __init__(self, attr, wrapperCls, data=None):
        """ Initialize with the attr to wrap, the cls and the data container attr """
        self.attr = attr
        self.wrapperCls = wrapperCls
        self.data = data
            
    def __getvalue__(self, obj):
        """ Return the attr value """
        data = getdata(obj, self.data)
        if self.attr not in data:
            data[self.attr] = self.wrapperCls()
        value = data[self.attr]
        setattr(obj, self.attr, value)
        return data[self.attr]
    
    def __set__(self, obj, value):
        """ Set the proper value for the attribute """
        data = getdata(obj, self.data)
        if not isinstance(value, self.wrapperCls):
            data[self.attr] = self.wrapperCls(value)
        else:
            data[self.attr] = value
        
    def __delete__(self, obj):
        """ Delete the value for the attribute """
        data = getdata(obj, self.data)
        del data[self.attr]