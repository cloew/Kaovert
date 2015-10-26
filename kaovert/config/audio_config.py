from .toml_attrs import toml_attrs, toml_lists
from .flex import FlexAttr
from kao_dict import KaoDict

@toml_lists('streams')
class AudioConfig(KaoDict):
    """ Represents the Audio Config for a Conversion Configuration """
    includeAll = FlexAttr('includeAll')