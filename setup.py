from setuptools import setup
from gopro_chapter_renamer import __version__

setup(
    name = 'gopro_renamer',
    author = 'Kevin Ha',
    version = __version__,
    py_modules = ['gopro_chapter_renamer'],
    entry_points = {
        'console_scripts': ['gopro_renamer = gopro_chapter_renamer:main']
    }
)
