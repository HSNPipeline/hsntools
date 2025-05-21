"""Setup script for convnwb."""

import os
from setuptools import setup, find_packages

# Get the current version number from inside the module
with open(os.path.join('convnwb', 'version.py')) as version_file:
    exec(version_file.read())

# Load the long description from the README
with open('README.rst') as readme_file:
    long_description = readme_file.read()

# Load the required dependencies from the requirements file
with open("requirements.txt") as requirements_file:
    install_requires = requirements_file.read().splitlines()

setup(
    name = 'convnwb',
    version = __version__,
    description = 'Helper code for converting data to NWB.',
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    python_requires = '>=3.7',
    packages = find_packages(),
    license = 'MIT License',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    platforms = 'any',
    project_urls = {
        'Documentation' : 'https://hsupipeline.github.io/convnwb/',
        'Bug Reports' : 'https://github.com/HSUPipeline/convnwb/issues',
        'Source' : 'https://github.com/HSUPipeline/convnwb',
    },
    download_url = 'https://github.com/HSUPipeline/convnwb/releases',
    keywords = ['neuroscience', 'single units', 'data management', 'neurodata without borders'],
    install_requires = install_requires,
    tests_require = ['pytest'],
    extras_require = {
        'compute' : ['scipy', 'scikit-learn'],
        'data' : ['pandas', 'h5py', 'pynwb'],
        'plot' : ['matplotlib'],
        'all' : ['scipy', 'scikit-learn', 'pandas', 'h5py', 'pynwb', 'matplotlib'],
    }
)