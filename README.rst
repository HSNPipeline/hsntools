convnwb
=======

|ProjectStatus|_ |BuildStatus|_

.. |ProjectStatus| image:: http://www.repostatus.org/badges/latest/active.svg
.. _ProjectStatus: https://www.repostatus.org/#active

.. |BuildStatus| image:: https://github.com/JacobsSU/convnwb/actions/workflows/build.yml/badge.svg
.. _BuildStatus: https://github.com/JacobsSU/convnwb/actions/workflows/build.yml

``convnwb`` is a small collection of helper code for converting data to the NWB format.

Overview
--------

This mini-module provides helper for converting data to NWB format.

This module contains general, task agnostic, utilities, and is expected to be used with the
`ConvertTEMPLATE <https://github.com/JacobsSU/ConvertTEMPLATE>`_.

Dependencies
------------

``convnwb`` is written in Python, and requires Python >= 3.6 to run.

It has the following required dependencies:

- `numpy <https://github.com/numpy/numpy>`_
- `scikit-learn <https://github.com/scikit-learn/scikit-learn>`_
- `pyyaml <https://github.com/yaml/pyyaml>`_
- `pynwb <https://github.com/NeurodataWithoutBorders/pynwb>`_

There are also optional dependencies, that offer extra functionality:

- `pytest <https://github.com/pytest-dev/pytest>`_ is needed to run the test suite locally

Installation
------------

This module should be installed from Github:

**Install from a clone**

First clone this repository, then move into the cloned repository, and install:

.. code-block:: shell

    $ git clone https://github.com/JacobsSU/convnwb
    $ cd convnwb
    $ pip install .
