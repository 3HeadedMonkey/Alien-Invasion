try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple alien invasion game',
    'author': 'Rafal Lukaszewski',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.'
    'author_email':'rafal.lukaszewski123@gmail.com.',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['Alien_Invasion','pygame'],
    'scripts': [],
    'name': 'Alien_Invasion'
        }
setup(**config)
