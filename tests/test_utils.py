import os.path
from datetime import datetime

import pytest

from src.utils import (get_database, change_date_to_datetime_type, sort_database_by_date,
                       delete_canceled_operations, encode_invoice)


def test_get_database():
    current_dir = os.path.dirname(__file__)
    data_for_test_path = os.path.join(current_dir, 'data_for_test.json')
    assert get_database(data_for_test_path) == [1, 2, 3, 4]


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


def test_delete_canceled_operations():
    assert delete_canceled_operations([{"state": "CANCELED"}, {"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]


@pytest.mark.parametrize('invoice, the_encode_invoice', [
    ('МИР 1234561234561234', 'МИР 1234 56** **** 1234'),
    ('Visa Platinum 1234561234561234', 'Visa Platinum 1234 56** **** 1234'),
    ('Счет 12341234123412341234', 'Счет **1234')
])
def test_encode_invoice(invoice, the_encode_invoice):
    assert encode_invoice(invoice) == the_encode_invoice
