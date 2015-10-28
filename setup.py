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
      version='0.1.0',
      description="",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['kaovert',
                'kaovert.args',
                'kaovert.commands',
                'kaovert.config',
                'kaovert.config.flex',
                'kaovert.conversion',
                'kaovert.conversion.hbclis'],
      scripts=['kaovert/scripts/kaovert'],
      **kwargs
     )