"""Packaging settings."""

import sys
from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from cusatexams import __version__

if sys.version_info < (3,0):
    sys.exit("cusatexams-cli requires python 3.")
    
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
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    package_data={"": ["LICENSE", "README.md"]},
    install_requires = ['docopt','requests', 'HTMLParser','texttable','ascii_graph','tqdm'],
    entry_points = {
        'console_scripts': [
            'cusatexams=cusatexams.cli:main',
        ],
    },
)
