import os.path

from src.utils import *

path_to_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
database_in_list = get_database(path_to_file)

database_formatted = change_date_to_datetime_type(database_in_list)

database_executed = delete_canceled_operations(database_formatted)

database_sorted = sort_database_by_date(database_formatted)
