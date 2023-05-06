"""Tests for convnwb.io.io"""

import os

import pandas as pd

from convnwb.tests.tobjects import TestTask
from convnwb.tests.tsettings import TEST_FILE_PATH

from convnwb.io.io import *

###################################################################################################
###################################################################################################

def test_save_nwbfile(tnwbfile):

    test_fname = 'test_nwbfile'
    save_nwbfile(tnwbfile, test_fname, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, test_fname + '.nwb'))

def test_load_nwbfile():

    test_fname = 'test_nwbfile'
    tnwbfile = load_nwbfile(test_fname, TEST_FILE_PATH)
    assert tnwbfile

def test_save_config():

    cdict1 = {'d1' : 1, 'd2' : 'name', 'd3' : ['a', 'b', 'c']}
    f_name1 = 'test_config1'
    save_config(cdict1, f_name1, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name1 + '.yaml'))

    cdict2 = {'d1' : 'words', 'd2' : None, 'd3' : ['list', 'of', 'terms']}
    f_name2 = 'test_config2'
    save_config(cdict2, f_name2, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name2 + '.yaml'))

def test_load_config():

    f_name1 = 'test_config1'
    config = load_config(f_name1, TEST_FILE_PATH)
    assert isinstance(config, dict)

def test_load_configs():

    f_names = ['test_config1', 'test_config2']
    configs = load_configs(f_names, TEST_FILE_PATH)
    assert isinstance(configs, dict)

def test_save_task_object():

    task = TestTask()
    f_name = 'task_obj'
    save_task_object(task, f_name, TEST_FILE_PATH)

    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.task'))

def test_load_task_object():

    f_name = 'task_obj'
    task = load_task_object(f_name, TEST_FILE_PATH)
    assert task

def test_save_txt():

    text = "Words, words, words."
    f_name = 'test_txt'

    save_txt(text, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.txt'))

def test_load_txt():

    f_name = 'test_txt'
    text = load_txt(f_name, TEST_FILE_PATH)
    assert text

def test_save_json():

    data = {'a' : 12, 'b' : 21}
    f_name = 'test_json'

    save_json(data, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.json'))

def test_load_json():

    f_name = 'test_json'
    data = load_json(f_name, TEST_FILE_PATH)
    assert data

def test_save_jsonlines():

    data = [{'A1' : {'a' : 12, 'b' : 21}},
            {'A2' : {'a' : 21, 'b' : 12}}]
    f_name = 'test_jsonlines'

    save_jsonlines(data, f_name, TEST_FILE_PATH)
    assert os.path.exists(os.path.join(TEST_FILE_PATH, f_name + '.json'))

def test_load_jsonlines():

    f_name = 'test_jsonlines'
    data = load_jsonlines(f_name, TEST_FILE_PATH)
    assert data
    assert isinstance(data, dict)
    assert isinstance(data[list(data.keys())[0]], dict)

def test_load_jsons_to_df():

    files = ['test_json', 'test_json']
    out = load_jsons_to_df(files, TEST_FILE_PATH)
    assert isinstance(out, pd.DataFrame)
    assert len(out) == len(files)

    # Test giving a file location
    out = load_jsons_to_df(TEST_FILE_PATH)
    assert isinstance(out, pd.DataFrame)

def test_read_h5file():

    f_name = 'test_hdf5'
    h5file = read_h5file(f_name, TEST_FILE_PATH)
    assert h5file
    h5file.close()

def test_open_h5file():

    f_name = 'test_hdf5'
    with open_h5file(f_name, TEST_FILE_PATH) as h5file:
        assert h5file

def test_load_from_h5file():

    f_name = 'test_hdf5'
    dataset = load_from_h5file('dataset', f_name, TEST_FILE_PATH)
    assert dataset is not None
