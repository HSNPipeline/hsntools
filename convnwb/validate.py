"""Helper utilities for validating NWB files."""

from convnwb.io import check_ext, check_folder
from convnwb.modutils import safe_import, check_dependency

pynwb = safe_import('pynwb')

###################################################################################################
###################################################################################################

@check_dependency(pynwb, 'pynwb')
def validate_nwb(file_name, folder=None, raise_error=True, verbose=False):
    """Validate a NWB file.

    Parameters
    ----------
    file_name : str or Path
        Name of the NWB file to validate.
    folder : str or Path, optional
        Name of the folder where the file is located.
    raise_error : boolean, optional, default: True
        Whether to raise an error if the NWB file fails validation.
    verbose : boolean, optional, default: True
        Whether to print out information about NWB validation.

    Returns
    -------
    errors : list or None
        A list of errors if any were found, None if no errors were found.

    Raises
    ------
    ValueError
        If there is an error in the NWB file. Only raised if `raise_error` is True.
    """

    file_name = check_folder(check_ext(file_name, '.nwb'), folder)
    with pynwb.NWBHDF5IO(file_name, 'r') as nwb_file:
        errors = pynwb.validate(nwb_file)

    if verbose:

        if errors:
            print('NWB errors: ')
            for error in errors:
                print('\t', error)
        else:
            print('NWB validation successful.')

    if raise_error and errors:

        raise ValueError('There is an issue with the NWB file.')

    return errors if errors else None
