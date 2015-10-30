try:
    from cx_Freeze import setup, Executable
    from enzyme.parsers import ebml
    import os
    
    kwargs = {'options':{"build_exe": {'packages':['kaovert'],
                                       'zip_includes':[(os.path.join(os.path.dirname(ebml.__file__), "specs/matroska.xml"), "enzyme/parsers/ebml/specs/matroska.xml")]}},
              'executables':[Executable('kaovert/scripts/kaovert')]
             }
    
except ImportError:
    from distutils.core import setup
    kwargs = {}

setup(name='kaovert',
      version='0.2.0',
      description="",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['kaovert',
                'kaovert.args',
                'kaovert.commands',
                'kaovert.config',
                'kaovert.conversion',
                'kaovert.conversion.hbclis'],
      scripts=['kaovert/scripts/kaovert'],
      install_requires = ['enzyme',
                          'flexconfig',
                          'jinja2',
                          'kao_command',
                          'kao_decorators',
                          'kao_toml'],
      **kwargs
     )