"""File I/O."""

import json
import pickle
import pathlib
from contextlib import contextmanager

import yaml

from convnwb.io.utils import get_files, check_ext, check_folder, make_session_name
from convnwb.modutils.dependencies import safe_import, check_dependency

sio = safe_import('.io', 'scipy')
pynwb = safe_import('pynwb')
pd = safe_import('pandas')
h5py = safe_import('h5py')

###################################################################################################
###################################################################################################

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


def save_jsonlines(data, file_name, folder=None):
    """Save out data to a JSONlines file.

    Parameters
    ----------
    data : list of dict
        Data to save out to a JSONlines file.
    file_name : str
        File name to give the saved out json file.
    folder : str or Path, optional
        Folder to save out to.
    """

    with open(check_ext(check_folder(file_name, folder), '.json'), 'a') as jsonlines_file:
        for cur_data in data:
            json.dump(cur_data, jsonlines_file)
            jsonlines_file.write('\n')


def load_jsonlines(file_name, folder=None):
    """Load from a JSON lines file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.

    Returns
    -------
    data : dict
        Loaded data from the JSONlines file.
    """

    all_data = {}
    with open(check_ext(check_folder(file_name, folder), '.json'), 'r') as jsonlines_file:
        for line in jsonlines_file:
            line_data = json.loads(line)
            key = list(line_data.keys())[0]
            all_data[key] = line_data[key]

    return all_data


@check_dependency(sio, 'scipy')
def load_matfile(file_name, folder=None, **kwargs):
    """Load a .mat file.

    Parameters
    ----------
    file_name : str
        File name of the file to load.
    folder : str or Path, optional
        Folder to load from.
    **kwargs
        Additional keywork arguments to pass into `scipy.io.loadmat`.

    Returns
    -------
    dict
        Loaded data from the matfile.

    Notes
    -----
    This function is a wrapper of `scipy.io.loadmat` and accepts
    any additional keyword arguments that `loadmat` accepts.
    """

    return sio.loadmat(check_ext(check_folder(file_name, folder), '.mat'), **kwargs)

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

## HDF5 FILE SUPPORT, INCLUDING CONTEXT MANAGERS

@check_dependency(h5py, 'h5py')
def read_h5file(file_name, folder=None, ext='.h5', **kwargs):
    """Read a hdf5 file.

    Parameters
    ----------
    file_name : str
        File name of the h5file to open.
    folder : str or Path, optional
        Folder to open the file from.
    ext : str, optional default: '.h5'
        The extension to check and use for the file.
    **kwargs
        Additional keyword arguments to pass into h5py.File.

    Returns
    -------
    h5file
        Open h5file object.

    Notes
    -----
    This function is a wrapper for `h5py.File`.
    """

    h5file = h5py.File(check_ext(check_folder(file_name, folder), ext), 'r', **kwargs)

    return h5file


@contextmanager
@check_dependency(h5py, 'h5py')
def open_h5file(file_name, folder=None, ext='.h5', **kwargs):
    """Context manager to open a hdf5 file.

    Parameters
    ----------
    file_name : str
        File name of the h5file to open.
    folder : str or Path, optional
        Folder to open the file from.
    ext : str, optional default: '.h5'
        The extension to check and use for the file.
    **kwargs
        Additional keyword arguments to pass into h5py.File.

    Yields
    ------
    h5file
        Open h5file object.

    Notes
    -----
    This function is a wrapper for `h5py.File`, creating a context manager.
    """

    h5file = read_h5file(file_name, folder, ext, **kwargs)

    try:
        yield h5file
    finally:
        h5file.close()


@check_dependency(h5py, 'h5py')
def load_from_h5file(field, file_name, folder=None, ext='.h5', **kwargs):
    """Load a specified field from a HDF5 file.

    Parameters
    ----------
    field : str
        Name of the field to load from the HDF5 file.
    file_name : str
        File name of the h5file to open.
    folder : str or Path, optional
        Folder to open the file from.
    ext : str, optional default: '.h5'
        The extension to check and use for the file.
    **kwargs
        Additional keyword arguments to pass into h5py.File.

    Returns
    -------
    data
        Loaded data field from the file.

    Notes
    -----
    This function uses `open_h5file` which itself wraps `h5py.File`.
    This function is useful for extracting a single data field.
    Files with multiple fields should be opened and accessed with `open_h5file`.
    """

    with open_h5file(file_name, folder, ext=ext, **kwargs) as h5file:
        output = h5file[field][:]

    return output
