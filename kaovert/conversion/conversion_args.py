from collections.abc import Mapping
import os

class ConversionArgs(Mapping):
    """ Represents the Conversion Arguments """
    
    def __init__(self, filename, index, **kwargs):
        """ Initialize with the filename, index, and other keyword arguments """
        self._dct = dict(kwargs)
        basename = os.path.basename(filename)
        filename, ext = os.path.splitext(basename)
        self._dct['filenameAndExt'] = basename
        self._dct['filename'] = filename
        self._dct['ext'] = ext[1:]
        self._dct['index'] = index
        
    def __getitem__(self, key):
        """ Return the arg value for the key """
        return self._dct[key]
    
    def __iter__(self):
        """ Return the iterator of the Arguments """
        return iter(self._dct)
    
    def __len__(self):
        """ Return the length of the Arguments """
        return len(self._dct)