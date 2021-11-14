import re
import ast
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/soorgeon/__init__.py', 'rb') as f:
    VERSION = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))

REQUIRES = [
    'jupytext',
    'parso',
    'nbformat',
    'jinja2',
    'pyyaml',
    'click',
]

DEV = [
    'pkgmt',
    'pytest',
    'yapf',
    'flake8',
    'invoke',
    'twine',
    'ipython',
    'ploomber',
    # to run some of the examples
    'pandas',
    'scikit-learn',
    'seaborn',
]

setup(
    name='soorgeon',
    version=VERSION,
    description=None,
    license=None,
    author=None,
    author_email=None,
    url=None,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={"": []},
    classifiers=[],
    keywords=[],
    install_requires=REQUIRES,
    extras_require={
        'dev': DEV,
    },
    entry_points={
        'console_scripts': ['soorgeon=soorgeon.cli:cli'],
    },
)
