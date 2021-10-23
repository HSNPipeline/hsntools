convnwb
=======

|ProjectStatus|_ |BuildStatus|_

.. |ProjectStatus| image:: http://www.repostatus.org/badges/latest/wip.svg
.. _ProjectStatus: https://www.repostatus.org/#wip

.. |BuildStatus| image:: https://github.com/JacobsSU/convnwb/actions/workflows/build.yml/badge.svg
.. _BuildStatus: https://github.com/JacobsSU/convnwb/actions/workflows/build.yml

`convnwb` is a small collection of helper code for converting data to the NWB format.

WARNING: This module is in early development, and may change at any time.

Overview
--------

This mini-module provides helper for converting data to NWB format.

This module contains utilities that are task agnostic, and is expected to be used with in the context of the
`ConvertTEMPLATE <https://github.com/JacobsSU/ConvertTEMPLATE>`_.

Dependencies
------------

``convnwb`` is written in Python, and requires Python >= 3.6 to run.

It has the following required dependencies:
- `pyyaml <https://github.com/yaml/pyyaml>`_

There are also optional dependencies, that offer extra functionality:

- `pytest <https://github.com/pytest-dev/pytest>`_ is needed to run the test suite locally

Installation
------------

This module should be installed from Github:
This module is currently in development, with no stable release version yet.

**Install from a clone**

First clone this repository, then move into the cloned repository, and install:

.. code-block:: shell

    $ git clone https://github.com/JacobsSU/convnwb
    $ cd convnwb
    $ pip install .
