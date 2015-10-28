from cx_Freeze import setup, Executable
from enzyme.parsers import ebml
import os

setup(name='kaovert',
      version='0.1.0',
      description="",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['kaovert',
                'kaovert.commands',
                'kaovert.config',
                'kaovert.conversion',
                'kaovert.conversion.hbclis',
                'kaovert.config.flex'],
      options = {"build_exe": {'packages':['kaovert'],
                               'zip_includes':[(os.path.join(os.path.dirname(ebml.__file__), "specs/matroska.xml"), "enzyme/parsers/ebml/specs/matroska.xml")]}},
      executables = [Executable('kaovert/scripts/kaovert')],
      scripts=['kaovert/scripts/kaovert']
     )