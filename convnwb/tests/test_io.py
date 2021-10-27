"""Tests for convnwb.io"""

from convnwb.tests.tsettings import TEST_FILE_PATH

from convnwb.io import *

###################################################################################################
###################################################################################################

def test_check_ext():

    f_name = 'test'
    ext = '.txt'

    out1 = check_ext(f_name, ext)
    assert out1 == 'test.txt'

    out2 = check_ext(f_name + '.txt', ext)
    assert out2 == 'test.txt'

def test_check_folder():

    folder = 'folder'
    f_name = 'file'

    out1 = check_folder(f_name, folder)
    assert out1 == 'folder/file'

    out2 = check_folder(f_name, None)
    assert out2 == 'file'

def test_drop_hidden_files():

    files = ['.', '.hidden', 'file_a', 'file_b']
    out = drop_hidden_files(files)
    assert out == ['file_a', 'file_b']

def test_ignore_files():

    files = ['data_1.txt', 'other.txt', 'data_2.txt', 'temp.txt']
    out = ignore_files(files, 'other')
    assert out == ['data_1.txt', 'data_2.txt', 'temp.txt']
    pass

def test_select_files():

    files = ['data_1.txt', 'other.txt', 'data_2.txt', 'temp.txt']
    out = select_files(files, 'data')
    assert out == ['data_1.txt', 'data_2.txt']

def test_get_files():

    out = get_files('.')
    assert isinstance(out, list)

def test_make_file_list():

    files = {'sub1' : ['session1', 'session2'], 'sub2' : ['session1']}
    out = make_file_list(files)
    assert isinstance(out, list)
    assert len(out) == 3
    for el in ['sub1_session1', 'sub1_session2', 'sub2_session1']:
        assert el in out

def test_save_config():
    pass

def test_load_config():
    pass

def test_load_configs():
    pass

def test_save_task_object():
    pass

def test_load_task_object():
    pass
