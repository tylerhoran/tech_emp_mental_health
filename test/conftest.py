import pandas as pd
import pytest


@pytest.fixture(scope='session')
def data():
    data_path = 'data/survey_data.csv'
    if data_path is None:
        pytest.fail("You must provide the --csv option on the command line")
    df = pd.read_csv(data_path)
    return df
