.. _api_documentation:

=================
API Documentation
=================

API reference for the module.

Table of Contents
=================

.. contents::
   :local:
   :depth: 2

File I/O
--------

Functions for file I/O.

NWB & Custom file I/O
~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.io.io
.. autosummary::
   :toctree: generated/

   save_nwbfile
   load_nwbfile
   save_config
   load_config
   load_configs
   save_object
   load_object

General file I/O
~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.io.io
.. autosummary::
   :toctree: generated/

   save_txt
   load_txt
   save_json
   load_json
   save_jsonlines
   load_jsonlines
   load_matfile
   load_jsons_to_df
   open_h5file
   save_to_h5file
   load_from_h5file

Utilities
~~~~~~~~~

.. currentmodule:: hsntools.io.utils
.. autosummary::
   :toctree: generated/

   get_files
   get_subfolders
   make_session_name
   make_file_list

Validate Functions
~~~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.io.validate
.. autosummary::
   :toctree: generated/

   validate_nwb

NSP
---

Functionality related to NSP (Neural Signal Processors).

I/O
~~~

.. currentmodule:: hsntools.nsp.io
.. autosummary::
   :toctree: generated/

   load_blackrock

Checks
~~~~~~

.. currentmodule:: hsntools.nsp.check
.. autosummary::
   :toctree: generated/

   check_blackrock_file_info

Objects
-------

Custom objects.

Electrodes
~~~~~~~~~~

.. currentmodule:: hsntools.objects.electrodes
.. autosummary::
   :toctree: generated/

   Electrodes

TaskBase
~~~~~~~~

.. currentmodule:: hsntools.objects.task
.. autosummary::
   :toctree: generated/

   TaskBase

Paths
-----

Path management.

Paths Object
~~~~~~~~~~~~

.. currentmodule:: hsntools.paths.paths
.. autosummary::
   :toctree: generated/

   Paths

Directory Creators
~~~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.paths.create
.. autosummary::
   :toctree: generated/

   make_folder
   create_project_directory
   create_subject_directory
   create_session_directory

Plots
-----

Plotting functions and utilities.

Timestamps
~~~~~~~~~~

.. currentmodule:: hsntools.plts.timestamps
.. autosummary::
   :toctree: generated/

   plot_alignment
   plot_peaks

Timestamps
----------

Functions and helpers for managing timestamps and temporal alignment.

Alignment
~~~~~~~~~

.. currentmodule:: hsntools.timestamps.align
.. autosummary::
   :toctree: generated/

   fit_sync_alignment
   predict_times
   predict_times_model
   match_pulses

Peaks
~~~~~

.. currentmodule:: hsntools.timestamps.peaks
.. autosummary::
   :toctree: generated/

   detect_peaks

Update
~~~~~~

.. currentmodule:: hsntools.timestamps.update
.. autosummary::
   :toctree: generated/

   offset_time
   change_time_units
   change_sampling_rate

Utils
~~~~~

.. currentmodule:: hsntools.timestamps.utils
.. autosummary::
   :toctree: generated/

   convert_samples_to_time
   create_timestamps_from_samples

Sorting
-------

Spike sorting related functionality.

I/O
~~~

.. currentmodule:: hsntools.sorting.io
.. autosummary::
   :toctree: generated/

   load_spike_data_file
   load_sorting_data_file
   save_units
   load_units

Processing
~~~~~~~~~~

.. currentmodule:: hsntools.sorting.process
.. autosummary::
   :toctree: generated/

   collect_all_sorting
   process_combinato_data

Utilities
~~~~~~~~~

.. currentmodule:: hsntools.sorting.utils
.. autosummary::
   :toctree: generated/

   get_group_labels
   get_sorting_kept_labels
   extract_clusters

Utils
-----

Utilities & helper functions.

Check Functions
~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.checks
.. autosummary::
   :toctree: generated/

   is_empty
   is_type
   check_str_contents
   clean_strings

Convert Functions
~~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.convert
.. autosummary::
   :toctree: generated/

   convert_str_to_bool
   convert_strlist_to_bool
   convert_type
   convert_to_array
   convert_time_to_date

Extract Functions
~~~~~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.extract
.. autosummary::
   :toctree: generated/

   get_event_time
   get_trial_value

Log Functions
~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.log
.. autosummary::
   :toctree: generated/

   print_status

Run Functions
~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.run
.. autosummary::
   :toctree: generated/

   catch_error

Tool Functions
~~~~~~~~~~~~~~

.. currentmodule:: hsntools.utils.tools
.. autosummary::
   :toctree: generated/

   incrementer
   get_current_date
