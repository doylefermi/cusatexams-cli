"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from cusatexams import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'cusatexams',
    version = __version__,
    description = 'Commandline application for exam.cusat.ac.in',
    long_description = long_description,
    url = 'https://github.com/doylefermi/cusatexams-cli',
    author = 'Doyle Fermi',
    author_email = 'doylefermi@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.x',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt','requests'],
    entry_points = {
        'console_scripts': [
            'cusatexams=cusatexams.cli:main',
        ],
    },
)
