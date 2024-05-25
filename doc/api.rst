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

.. currentmodule:: convnwb.io.io
.. autosummary::
   :toctree: generated/

   save_nwbfile
   load_nwbfile
   save_config
   load_config
   load_configs
   save_task_object
   load_task_object

General file I/O
~~~~~~~~~~~~~~~~

.. currentmodule:: convnwb.io.io
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

.. currentmodule:: convnwb.io.utils
.. autosummary::
   :toctree: generated/

   get_files
   get_subfolders
   make_session_name
   make_file_list

Checks
~~~~~~

.. currentmodule:: convnwb.io.check
.. autosummary::
   :toctree: generated/

   check_blackrock_file_info

Validate Functions
~~~~~~~~~~~~~~~~~~

.. currentmodule:: convnwb.io.validate
.. autosummary::
   :toctree: generated/

   validate_nwb

Objects
-------

Custom objects.

Electrodes
~~~~~~~~~~

.. currentmodule:: convnwb.objects.electrodes
.. autosummary::
   :toctree: generated/

   Electrodes

TaskBase
~~~~~~~~

.. currentmodule:: convnwb.objects.task
.. autosummary::
   :toctree: generated/

   TaskBase

Paths
-----

Path management.

Paths Object
~~~~~~~~~~~~

.. currentmodule:: convnwb.paths.paths
.. autosummary::
   :toctree: generated/

   Paths

Directory Creators
~~~~~~~~~~~~~~~~~~

.. currentmodule:: convnwb.paths.create
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

.. currentmodule:: convnwb.plts.timestamps
.. autosummary::
   :toctree: generated/

   plot_alignment
   plot_peaks

Timestamps
----------

Functions and helpers for managing timestamps and temporal alignment.

Alignment
~~~~~~~~~

.. currentmodule:: convnwb.timestamps.align
.. autosummary::
   :toctree: generated/

   fit_sync_alignment
   predict_times
   predict_times_model
   match_pulses

Peaks
~~~~~

.. currentmodule:: convnwb.timestamps.peaks
.. autosummary::
   :toctree: generated/

   detect_peaks

Update
~~~~~~

.. currentmodule:: convnwb.timestamps.update
.. autosummary::
   :toctree: generated/

   offset_time
   change_time_units
   change_sampling_rate

Sorting
-------

Spike sorting related functionality.

I/O
~~~

.. currentmodule:: convnwb.sorting.io
.. autosummary::
   :toctree: generated/

   load_spike_data_file
   load_sorting_data_file
   save_units
   load_units

Processing
~~~~~~~~~~

.. currentmodule:: convnwb.sorting.io
.. autosummary::
   :toctree: generated/

   collect_all_sorting
   process_combinato_data

Utilities
~~~~~~~~~

.. currentmodule:: convnwb.sorting.utils
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

.. currentmodule:: convnwb.utils.checks
.. autosummary::
   :toctree: generated/

   is_empty
   is_type
   check_str_contents
   clean_strings

Convert Functions
~~~~~~~~~~~~~~~~~

.. currentmodule:: convnwb.utils.convert
.. autosummary::
   :toctree: generated/

   convert_str_to_bool
   convert_strlist_to_bool
   convert_type
   convert_to_array
   convert_time_to_date

Extract Functions
~~~~~~~~~~~~~~~~~

.. currentmodule:: convnwb.utils.extract
.. autosummary::
   :toctree: generated/

   get_event_time
   get_trial_value

Log Functions
~~~~~~~~~~~~~

.. currentmodule:: convnwb.utils.log
.. autosummary::
   :toctree: generated/

   print_status

Run Functions
~~~~~~~~~~~~~

.. currentmodule:: convnwb.utils.run
.. autosummary::
   :toctree: generated/

   catch_error

Tool Functions
~~~~~~~~~~~~~~

.. currentmodule:: convnwb.utils.tools
.. autosummary::
   :toctree: generated/

   incrementer
   get_current_date
