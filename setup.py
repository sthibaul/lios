from distutils.core import setup
from glob import glob
setup(name='lios',
      version='2.0',
      description='Python Distribution Utilities',
      author='Nalin.x.Linux',
      author_email='Nalin.x.Linux@gmail.com',
      url='https://github.com/Nalin-x-Linux/',
      license = 'GPL-3',
      packages=['lios','lios/ocr','lios/scanner','lios/ui/','lios/ui/gtk'],
      data_files=[('share/lios/',['share/lios/readme','share/lios/lios']),('share/applications/',['share/applications/Lios.desktop']),('bin',['bin/lios'])]
      )
# sudo python3 setup.py install --install-data=/usr
