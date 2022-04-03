"""Functions and utilities for working  with timestamps."""

import numpy as np

from convnwb.modutils import safe_import, check_dependency

sklearn = safe_import('sklearn')

###################################################################################################
###################################################################################################

@check_dependency(sklearn, 'sklearn')
def align_times(sync_behavioral, sync_neural, score_thresh=0.9999,
                ignore_poor_alignment=False, return_model=False, verbose=False):
    """Align times across different recording systems.

    Parameters
    ----------
    sync_behavioral : 1d array
        Sync pulse times from behavioral computer.
    sync_neural : 1d array
        Sync pulse times from neural computer.
    score_thresh : float, optional, default: 0.9999
        R^2 threshold value to check that the fit model is better than.
    ignore_poor_alignment : bool, optional, default: False
        Whether to ignore a bad alignment score.
    return_model : bool, optional, default: False
        Whether to return the model object. If False, returns
    verbose : bool, optional, default: False
        Whether to print out model information.

    Returns
    -------
    model : LinearRegression
        The fit model object. Only returned if `return_model` is True.
    model_intercept : float
        Intercept of the model predicting differences between sync pulses.
        Returned if `return_model` is False.
    model_coef : float
        Learned coefficient of the model predicting  differences between sync pulses.
        Returned if `return_model` is False.
    score : float
        R^2 score of the model, indicating how good a fit there is between sync pulses.
    """

    # sklearn imports are weird, so re-import here
    #   the sub-modules here aren't available from the global namespace
    from sklearn.metrics import r2_score
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    # Reshape to column arrays for scikit-learn
    sync_behavioral = sync_behavioral.reshape(-1, 1)
    sync_neural = sync_neural.reshape(-1, 1)

    # Linear model to predict alignment between time traces
    x_train, x_test, y_train, y_test = train_test_split(\
        sync_behavioral, sync_neural, test_size=0.50, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    score = r2_score(y_test, y_pred)
    bad_score_msg = 'This session has bad synchronization between brain and behavior'
    if score < score_thresh:
        if not ignore_poor_alignment:
            raise ValueError(bad_score_msg)
        else:
            print(bad_score_msg)

    if verbose:
        print('coef', model.coef_[0], '\n intercept', model.intercept_[0])
        print('score', score)

    if return_model:
        return model, score
    else:
        return model.intercept_[0], model.coef_[0][0], score


def predict_times(times, intercept, coef):
    """Predict times alignment from model coefficients.

    Parameters
    ----------
    times : 1d array
        Timestamps to align.
    intercept : float
        Learned intercept of the model predicting differences between sync pulses.
    coef : float
        Learned coefficient of the model predicting  differences between sync pulses.

    Returns
    -------
    1d array
        Predicted times, after applying time alignment.
    """

    return coef * np.array(times).astype(float) + intercept


def predict_times_model(times, model):
    """Predict times alignment from a model object.

    Parameters
    ----------
    times : 1d array
        Timestamps to align.
    model : LinearRegression
        A model object, with a fit model predicting timestamp alignment.

    Returns
    -------
    1d array
        Predicted times, after applying time alignment.
    """

    return model.predict(times.reshape(-1, 1))
