import os.path
from datetime import datetime

import pytest

from src.utils import get_database, change_date_to_datetime_type


def test_get_database():
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_FOR_TEST_PATH = os.path.join(CURRENT_DIR, 'data_for_test.json')
    assert get_database(DATA_FOR_TEST_PATH) == [1, 2, 3, 4]


@pytest.mark.parametrize('array, result', [
    ([{'date': '2019-08-26T10:50:58.294041'}],
     [{'date': datetime(2019, 8, 26, 10, 50, 58, 294041)}]),
    ([{'id': 4}], [])
])
def test_change_date_to_datetime_type(array, result):
    assert change_date_to_datetime_type(array) == result
