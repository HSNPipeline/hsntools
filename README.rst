convnwb
=======

|ProjectStatus| |BuildStatus| |Coverage|

.. |ProjectStatus| image:: http://www.repostatus.org/badges/latest/active.svg
   :target: https://www.repostatus.org/#active
   :alt: project status

.. |BuildStatus| image:: https://github.com/HSUPipeline/convnwb/actions/workflows/build.yml/badge.svg
   :target: https://github.com/HSUPipeline/convnwb/actions/workflows/build.yml
   :alt: build statue

.. |Coverage| image:: https://codecov.io/gh/HSUPipeline/convnwb/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/HSUPipeline/convnwb
   :alt: coverage

``convnwb`` is a module of code to help with converting data to the NWB format.

Overview
--------

This module contains general, task agnostic, utilities, for converting data to the
`NWB <https://www.nwb.org/>`_ format.

Available sub-modules in `convnwb` include:

- ``io``: includes save and load functions and utilities for working with files through the conversion process
- ``nsp``: includes functionality that relating to managing recording files from neural signal processors
- ``objects``: includes objects for storing relevant data, for example electrode or task related information
- ``paths``: includes a `Paths` object and utilities for defining and using a consistent path structure
- ``plts``: includes plot functions for examining data through the conversion process
- ``sorting``: includes functionality relating to managing recording spike sorting
- ``timestamps``: includes utilities for managing timestamps and aligning data streams
- ``utils``: includes general utilities for working with data through the conversion process

For converting data, `convnwb` can be used together with the
`ConvertTEMPLATE <https://github.com/HSUPipeline/ConvertTEMPLATE>`_.

Dependencies
------------

``convnwb`` is written in Python, and requires Python >= 3.6 to run.

It has the following required dependencies:

- `numpy <https://github.com/numpy/numpy>`_
- `pyyaml <https://github.com/yaml/pyyaml>`_

There are also optional dependencies, that offer extra functionality:

- `pynwb <https://github.com/NeurodataWithoutBorders/pynwb>`_ is needed for validating NWB files
- `matplotlib <https://github.com/matplotlib/>`_ is needed for making plots to check conversions
- `scikit-learn <https://github.com/scikit-learn/scikit-learn>`_ is needed to aligning sync pulses
- `pandas <https://github.com/pandas-dev/pandas>`_ is needed for utilities that load dataframes
- `scipy <https://github.com/scipy/scipy>`_ is needed for some load and timestamp related functions
- `h5py <https://github.com/h5py/h5py>`_ is needed for utilities that open HDF5 files
- `neo <https://github.com/NeuralEnsemble/python-neo>`_ is needed for loading & interacting with NSP files
- `mat73 <https://github.com/skjerns/mat7.3>`_ is needed for loading .mat files version >= 7.3
- `pytest <https://github.com/pytest-dev/pytest>`_ is needed to run the test suite locally

Installation
------------

The current release version is the 0.3.X series.

Check the
`changelog <https://github.com/HSUPipeline/convnwb/blob/main/CHANGELOG.md>`_
for notes on updates and changes across versions.

This module should be installed from Github:

**Install from a clone**

First clone this repository, then move into the cloned repository, and install:

.. code-block:: shell

    $ git clone https://github.com/HSUPipeline/convnwb
    $ cd convnwb
    $ pip install .

Contribute
----------

This project welcomes and encourages contributions from the community!

To file bug reports and/or ask questions about this project, please use the
`Github issue tracker <https://github.com/HSUPipeline/convnwb/issues>`_.

When interacting with this project, please follow the
`code of conduct <https://github.com/HSUPipeline/convnwb/blob/main/CODE_OF_CONDUCT.md>`_.
