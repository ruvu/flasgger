# Fix for older setuptools
import re
import os

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read('README.md')


# grep flasgger/__init__.py since python 3.x cannot
# import it before using 2to3
file_text = read(fpath('flasgger/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval



d = generate_distutils_setup(
    packages=['flasgger'],
)

setup(**d)