"""Utility functions for managing files."""

import os
import json
import pickle
import pathlib

import yaml

from convnwb.modutils import safe_import, check_dependency

pynwb = safe_import('pynwb')
pd = safe_import('pandas')

###################################################################################################
###################################################################################################

### FILE UTILITIES

def check_ext(file_name, ext):
    """Check the extension for a file name, and add if missing.

    Parameters
    ----------
    file_name : str
        The name of the file.
    ext : str
        The extension to check and add.

    Returns
    -------
    str
        File name with the extension added.
    """

    return file_name + ext if not file_name.endswith(ext) else file_name


def drop_ext(file_name):
    """Drop the extension from a file name.

    Parameters
    ----------
    file_name : str
        File name, potentially including a file extension.

    Returns
    -------
    file_name : str
        File name, without the file extension.
    """

    return file_name.split('.')[0]


def check_folder(file_name, folder):
    """Check a file name, adding folder path if needed.

    Parameters
    ----------
    file_name : str
        The name of the file.
    folder : str or Path, optional
        Folder location of the file.

    Returns
    -------
    str
        Full path of the file.
    """

    return os.path.join(folder, file_name) if folder else file_name


def drop_hidden_files(files):
    """Clean hidden files from a list of files.

    Parameters
    ----------
    files : list of str
        List of file names.

    Returns
    -------
    list of str
        List of file names with hidden files dropped.
    """

    return [file for file in files if file[0] != '.']


def drop_file_extensions(files):
    """Drop the file extensions from a list of file names.

    Parameters
    ----------
    files : list of str
        List of file names.

    Returns
    -------
    list of str
        List of file names with extensions dropped.
    """

    return [drop_ext(file) for file in files]


def ignore_files(files, ignore):
    """Ignore files based on a search term of interest.

    Parameters
    ----------
    files : list of str
        List of file names.
    ignore : str
        String to use to drop files from list.

    Returns
    -------
    list of str
        List of file names with ignored files dropped.
    """

    return [file for file in files if ignore not in file]


def select_files(files, search):
    """Select files based on a search term of interest.

    Parameters
    ----------
    files : list of str
        List of file names.
    search : str
        String to use to keep files.

    Returns
    -------
    list of str
        List of file names with selected files kept.
    """

    return [file for file in files if search in file]


def sort_files(files):
    """Sort a list of file names.

    Parameters
    ----------
    files : list of str
        List of file names.

    Returns
    -------
    list of str
        Sorted list of file names.
    """

    return sorted(files)


def make_session_name(experiment, subject, session):
    """Create a standardized session name.

    Parameters
    ----------
    subject : str
        The subject label.
    experiment : str, optional
        Name of the experiment.
    session : str or int
        The session number.
        Can be an integer index, or a string, for example `session_0`.
    add_ext : bool, optional, default: False
        Whether to add the NWB extension to the file name.

    Returns
    -------
    session_name : str
        The session name.

    Notes
    -----
    The standard session name is structured as: 'EXPERIMENT_SUBJECT_session_#'
    Note that this is a flip of the experiment / subject order in the path layout.
    """

    session = 'session_' + str(session) if 'session' not in str(session) else session
    session_name = '_'.join([experiment, subject, session])

    return session_name


def make_file_list(experiment, files, ext=None):
    """Make a list of subject files.

    Parameters
    ----------
    experiment : str
        Name of the experiment.
    files : dict
        Collection of files per subject.
    ext : str, optional
        Extension name to add to the file list.

    Returns
    -------
    file_lst : list of str
        List of all subject files.
    """

    file_list = []
    for subject, sessions in files.items():
        for session in sessions:
            file_name = '_'.join([experiment, subject, session])
            file_name = check_ext(file_name, ext) if ext else file_name
            file_list.append(file_name)

    return file_list


def file_in_list(file_name, file_list, drop_extensions=True):
    """Check whether a given file name is in a list of file names.

    Parameters
    ----------
    file_name : str
        File name.
    file_list : list of str
        List of file names.
    drop_extensions : bool, optional, default: True
        Whether to drop any extensions before doing the comparison.

    Returns
    -------
    bool
        Indicator of whether the file name is in the list of file names.
    """

    if drop_extensions:
        file_name = drop_ext(file_name)
        file_list = drop_file_extensions(file_list)

    output = False
    if file_name in file_list:
        output = True

    return output


def missing_files(file_list, compare):
    """Check for missing files - those that are in a given list but not in a comparison list.

    Parameters
    ----------
    file_list : list of str
        List of files to check.
    compare : list of str
        List of files to compare to.

    Returns
    -------
    list of str
        Any files from `file_list` that are not in `compare`.
    """

    return list(set(file_list) - set(compare))

### FILE I/O

def get_files(folder, select=None, ignore=None, drop_hidden=True, sort=True, drop_extensions=False):
    """Get a list of files from a directory.

    Parameters
    ----------
    folder : str or Path
        Name of the folder to get the list of files from.
    select : str, optional
        A search string to use to select files.
    ignore : str, optional
        A search string to use to drop files.
    drop_hidden : bool, optional, default: True
        Whether to drop hidden files from the list.
    sort : bool, optional, default: True
        Whether to sort the list of file names.
    drop_extensions : bool, optional, default: False
        Whether the drop the file extensions from the returned file list.

    Returns
    -------
    list of str
        A list of files from the folder.
    """

    files = os.listdir(folder)

    # If requested, drop any hidden files (leading .'s)
    if drop_hidden:
        files = drop_hidden_files(files)

    # If requested, filter files to those that containing given search terms
    if select:
        files = select_files(files, select)

    # If requested, filter files to ignore any containing given search terms
    if ignore:
        files = ignore_files(files, ignore)

    # If requested, sort the list of files
    if sort:
        files = sort_files(files)

    if drop_extensions:
        files = drop_file_extensions(files)

    return files


#### NWB FILES

@check_dependency(pynwb, 'pynwb')
def save_nwbfile(nwbfile, file_name, folder=None):
    """Save out an NWB file.

    Parameters
    ----------
    file_name : str or dict
        The file name to load.
        If dict, is passed into `make_session_name` to create the file name.
    folder : str
        The folder to load the file from.
    """

    if isinstance(file_name, dict):
        file_name = make_session_name(**file_name)

    with pynwb.NWBHDF5IO(check_ext(check_folder(file_name, folder), '.nwb'), 'w') as io:
        io.write(nwbfile)


@check_dependency(pynwb, 'pynwb')
def load_nwbfile(file_name, folder=None, return_io=False):
    """Load an NWB file.

    Parameters
    ----------
    file_name : str or dict
        The file name to load.
        If dict, is passed into `make_session_name` to create the file name.
    folder : str
        The folder to load the file from.
    return_io : bool, optional, default: False
        Whether to return the pynwb IO object.

    Returns
    -------
    nwbfile : pynwb.file.NWBFile
        The NWB file object.
    io : pynwb.NWBHDF5IO
        The IO object for managing the file status.
        Only returned if `return_io` is True.
    """

    if isinstance(file_name, dict):
        file_name = make_session_name(**file_name)

    io = pynwb.NWBHDF5IO(check_ext(check_folder(file_name, folder), '.nwb'), 'r')
    nwbfile = io.read()

    if return_io:
        return nwbfile, io
    else:
        return nwbfile

#### CONFIG FILES

def save_config(cdict, file_name, folder=None):
    """Save out a config file.

    Parameters
    ----------
    cdict : dict
        Dictionary of information to save to the config file.
    file_name : str
        File name to give the saved out config file.
    folder : str or Path, optional
        Folder to save the config file to.
    """

    with open(check_ext(check_folder(file_name, folder), '.yaml'), 'w') as file:
        yaml.dump(cdict, file)


def load_config(file_name, folder=None):
    """Load an individual config file.

    Parameters
    ----------
    file_name : str
        Name of the config file to load.
    folder : str or Path, optional
        Folder to load the config file from.

    Returns
    -------
    data : dict
        Information from the loaded config file.
    """

    with open(check_ext(check_folder(file_name, folder), '.yaml'), 'r') as fobj:
        data = yaml.safe_load(fobj)

    return data


def load_configs(files, folder=None):
    """Load all configs together.

    Parameters
    ----------
    files : list of str
        Names of all the config files to load.
    folder : str or Path, optional
        Folder to load the config files from.

    Returns
    -------
    configs : dict
        Information from the config files.
    """

    configs = {}
    for file in files:
        label = file.split('_')[0]
        configs[label] = load_config(file, folder=folder)

    return configs


### TASK OBJECTS

def save_task_object(task, file_name, folder=None):
    """Save a task object.

    Parameters
    ----------
    task : Task
        Task object to save out.
    file_name : str
        File name to give the saved out task file.
    folder : str or Path, optional
        Folder to save out to.

    Notes
    -----
    Task objects are saved and loaded as pickle files.
    """

    with open(check_ext(check_folder(file_name, folder), '.task'), 'wb') as fobj:
        pickle.dump(task, fobj)


def load_task_object(file_name, folder=None):
    """Load a task object.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    task
        Loaded task object.

    Notes
    -----
    Task objects are saved and loaded as pickle files.
    """

    with open(check_ext(check_folder(file_name, folder), '.task'), 'rb') as load_obj:
        task = pickle.load(load_obj)

    return task


## OTHER FILE I/O

def save_txt(text, file_name, folder=None):
    """Save out text to a txt file.

    Parameters
    ----------
    text : str
        Text to save out to a txt file.
    file_name : str
        File name to give the saved out txt file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.txt'), 'w') as txt_file:
        txt_file.write(text)


def load_txt(file_name, folder=None):
    """Load text from a txt file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    text : str
        Loaded text from the txt file.
    """

    with open(check_ext(check_folder(file_name, folder), '.txt')) as txt_file:
        text = txt_file.readlines()

    return text


def save_json(data, file_name, folder=None):
    """Save out a dictionary of data to a JSON file.

    Parameters
    ----------
    data : dict
        Data to save out to a JSON file.
    file_name : str
        File name to give the saved out json file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.json'), 'w') as json_file:
        json.dump(data, json_file)


def load_json(file_name, folder=None):
    """Load from a JSON file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    data : dict
        Loaded data from the JSON file.
    """

    with open(check_ext(check_folder(file_name, folder), '.json')) as json_file:
        data = json.load(json_file)

    return data

## LOAD COLLECTIONS OF FILES TOGETHER

@check_dependency(pd, 'pandas')
def load_jsons_to_df(files, folder=None):
    """Load a collection of JSON files into a dataframe.

    Parameters
    ----------
    files : list of str or str or Path
        If list, should be a list of file names to load.
        If str or Path, should be a folder name, from which all JSON files will be loaded.
    folder : str or Path, optional
        Folder location to load the files from.
        Only used if `files` is a list of str.

    Returns
    -------
    df : pd.DataFrame
        A dataframe containing the data from the JSON files.
    """

    if isinstance(files, (str, pathlib.PosixPath)):
        files = get_files(folder, select='json')

    file_data = [load_json(file, folder=folder) for file in files]

    df = pd.DataFrame(file_data)

    return df
