from distutils.core import setup

setup(name='kaovert',
      version='0.0.1',
      description="",
      author='',
      author_email='',
      packages=['kaovert',
                'kaovert.commands',
                'kaovert.config'],
      scripts=['kaovert/scripts/kaovert']
     )