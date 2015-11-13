from kao_decorators import proxy_for

@proxy_for('_items', ['__iter__', '__contains__', '__getitem__', 'append', 'extend'])
class ListArg:
    """ Represents a list of args taht hsould be returned as a comma separated list """
    
    def __init__(self, items=None):
        """ Initialize with the items """
        self._items = items if items is not None else []
        
    def build(self):
        """ Return the argument """
        return ",".join(self._items)