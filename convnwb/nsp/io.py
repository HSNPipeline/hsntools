"""NSP related I/O functions."""

from convnwb.io.utils import check_folder
from convnwb.modutils.dependencies import safe_import, check_dependency

neo = safe_import('neo')

###################################################################################################
###################################################################################################

@check_dependency(neo, 'neo')
def load_blackrock(file_name, folder, nsx_to_load=None, load_nev=None):
    """Load a set of Blackrock files.

    Parameters
    ----------
    file_name : str
        The file name to load.
    folder : str or Path
        The folder to load the file(s) from.
    nsx_to_load : int or list, optional
        Which nsx file(s) to load.
    load_nev : bool, optional, default: True
        Whether to load the nev file.

    Returns
    -------
    reader : neo.rawio.blackrockrawio.BlackrockRawIO
        Blackrock file reader.
    """

    reader = neo.rawio.BlackrockRawIO(\
        check_folder(file_name, folder), nsx_to_load=nsx_to_load, load_nev=load_nev)
    reader.parse_header()

    return reader
