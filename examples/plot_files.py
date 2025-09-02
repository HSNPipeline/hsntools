"""
Directories & File Management
=============================

Manage files & directories for human single-neuron projects.

This example introduces and explores the file management and directory structure functionality
of `hsntools`.
"""

###################################################################################################
# Creating Standardized Directory Structures
# ------------------------------------------
#
# The HSNPipeline, through `hsntools` defines a standardized directory structure for managing
# files that are part of a Human-Single Neuron project.
#
# If you use this standardized directory structure, then `hsntools` will be aware of this
# organization and be able to navigate the various files.
#
# This example explores how to automatically set up the standardized directory and how to
# use the HSNPipeline Paths object to navigate the structure.
#

# sphinx_gallery_thumbnail_number = 1

# Import paths related functionality
from hsntools.paths import Paths
from hsntools.paths import (create_project_directory,
                            create_subject_directory,
                            create_session_directory)

###################################################################################################
#
# First, we will define an example project definition and associated directory structure.
#
# The directory uses the following organization
# - `project`: the overall project title
# - `subject`: subjects that are part of the project, each with their own subject code
# - `experiment`: the task or tasks that each subject completes
# - `session:` individual sessions of the task that the subject completes
#

###################################################################################################

# Define settings for creating a project structure
project = 'tproj'
subject = 'subj1'
experiments = ['task1', 'task2']
exp1_sessions = [0, 1]
exp2_sessions = 'session_0'

###################################################################################################
#
# Now we can initialize folder structures for each element of our project.
#
# To do so, we can use the following functions:
# - :func:`~.create_project_directory` to initialize a project directory structure
# - :func:`~.create_subject_directory` to initialize a new subject directory structure
# - :func:`~.create_session_directory` to initialize a new session directory structure
#

###################################################################################################

# Create a base project directory
create_project_directory('.', project)

###################################################################################################

# Create an example subject directory
create_subject_directory(project, subject, experiments=experiments)

###################################################################################################

# Create an example session directory for the first task
create_session_directory(project, subject, 'task1', exp1_sessions)

###################################################################################################

# Create an session directory for the second task
create_session_directory(project, subject, 'task2', exp2_sessions)

###################################################################################################
#
# In the above, we defined a set of repository structures to initialize the project, experiments,
# subjects, and sessions. If you check your local file system, you will see new folders have
# been created.
#
# Note that in the above we created each layer individually, but this is not required. If you
# want to add a session for a new session of a new subject (or new experiment) you can use
# the `create_session_directory` function directly, and missing layers will be created.
#

###################################################################################################
# Using the hsntools Paths object
# -------------------------------
#
# In the above section we initialized directory structures as defined by the standard
# structure defined and used by `hsntools` and the HSNPipeline more broadly.
#
# To interact with this structure, we can use the :class:`~.Paths` object.
#
# A Paths object can be defined with specific tasks and sessions, and then used to access the
# files for that session, without needing to explicitly define any paths (assuming the standard
# directory structure has been used and files are in the correct folders).
#

###################################################################################################

# Create a paths object defined with our subject and session information
paths = Paths('./tproj', subject, experiment=experiments[0], session=0)

###################################################################################################

# Print the directory structure from the paths object
paths.print_structure()

###################################################################################################
#
# The Paths object can also be used to check and access files within particular folders of the
# directory structure, by checking particular locations and getting individual files.
#

###################################################################################################

# Get a list of sub-folders in the 'recordings' folder
paths.get_subfolders('recordings')

###################################################################################################

# Get a list of files in the 'docs' sub-folder
paths.get_files('docs')

###################################################################################################
#
# You can also use the Paths object to check where all of the path names and folder structures.
#

###################################################################################################

# Get a list of all the paths
print(paths.all_paths)

###################################################################################################

# Get a list of all the folders
print(paths.all_folders)

###################################################################################################
