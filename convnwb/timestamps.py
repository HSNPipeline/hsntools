"""Functions and utilities for working  with timestamps."""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

###################################################################################################
###################################################################################################

def align_times(sync_behavioral, sync_neural, score_thresh=0.9999, return_model=False, verbose=False):
    """Align times across different recording systems.

    Parameters
    ----------
    sync_behavioral : 1d array
        Sync pulse times from behavioral computer.
    sync_neural : 1d array
        Sync pulse times from neural computer.
    score_thresh : float, optional, default: 0.9999
        R^2 threshold value to check that the fit model is better than.
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

    # Reshape to column arrays for scikit-learn
    sync_behavioral = sync_behavioral.reshape(-1, 1)
    sync_neural = sync_neural.reshape(-1, 1)

    # Linear model to predict alignment between time traces
    x_train, x_test, y_train, y_test = train_test_split(sync_behavioral, sync_neural,
                                                        test_size=0.50, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    score = r2_score(y_test, y_pred)
    if score < score_thresh:
        raise ValueError('This session has bad synchronization between brain and behavior')

    if verbose == True:
        print('coef', model.coef_, '\n intercept', model.intercept_)
        print('score', score)

    if return_model:
        return model, score
    else:
        return model.intercept_, model.coef_, score


def predict_times_model(model, times):
    """Predict times alignment from a model object.

    Parameters
    ----------
    model : LinearRegression
        A model object, with a fit model predicting timestamp alignment.
    times : 1d array
        Timestamps to align.

    Returns
    -------
    predicted_times : 1d array
        Predicted times, after applying time alignment.
    """

    aligned_times = model.predict(times.reshape(-1, 1))

    return predicted_times


def predict_times_coef(offset, coef, times):
    """Predict times alignment from learned model coefficients.

    Parameters
    ----------
    intercept : float
        Learned intercept of the model predicting differences between sync pulses.
    coef : float
        Learned coefficient of the model predicting  differences between sync pulses.
    times : 1d array
        Timestamps to align.

    Returns
    -------
    predicted_times : 1d array
        Predicted times, after applying time alignment.
    """

    predicted_times = coef * times + intercept

    return predicted_times
