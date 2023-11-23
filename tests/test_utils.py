import os.path
from datetime import datetime

import pytest

from src.utils import get_database, change_date_to_datetime_type, sort_database_by_date


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


@pytest.mark.parametrize('origin_lst, sorted_lst', [
    ([{'date': datetime(2019, 8, 26, 10, 50, 58, 0)},
      {'date': datetime(2018, 4, 4, 17, 33, 34, 0)}],
     [{'date': datetime(2018, 4, 4, 17, 33, 34, 0)},
      {'date': datetime(2019, 8, 26, 10, 50, 58, 0)}])
            ])
def test_sort_database_by_date(origin_lst, sorted_lst):
    assert sort_database_by_date(origin_lst) == sorted_lst
