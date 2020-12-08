from setuptools import setup, find_packages

setup(name='cmstool',
      version='0.1b',
      description='Cable Modem Statistics Tool',
      url='https://github.com/charlysan/cmstool/',
      entry_points={
        'console_scripts': [
            'cmscraper_cli = cmscraper.cmscraper_cli:main'
        ]
      },
      author='charlysan',
      author_email='chrlysn0@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['argparse ~= 1.4.0', 'requests ~= 2.25.0', 'BeautifulSoup4 ~= 4.9.3', 'bs4 ~= 0.0.1'])