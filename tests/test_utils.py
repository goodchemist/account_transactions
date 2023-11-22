import os.path
from src.utils import get_database


def test_get_database():
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_FOR_TEST_PATH = os.path.join(CURRENT_DIR, 'data_for_test.json')
    assert get_database(DATA_FOR_TEST_PATH) == [1, 2, 3, 4]
