from .toml_attrs import toml_attrs, toml_lists
from kao_dict import KaoDict

@toml_attrs('includeAll')
@toml_lists('tracks')
class SubtitleConfig(KaoDict):
    """ Represents the Subtitle Configuration """