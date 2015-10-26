from distutils.core import setup

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
      scripts=['kaovert/scripts/kaovert']
     )