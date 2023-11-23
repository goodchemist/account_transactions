import os.path

from src.utils import *

path_to_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
database_in_list = get_database(path_to_file)
database_formatted = change_date_to_datetime_type(database_in_list)
