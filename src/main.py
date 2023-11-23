import os.path

from src.utils import *

# load information from a json-file
path_to_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
database_in_list = get_database(path_to_file)

# change date for each transaction to datetime type
database_formatted = change_date_to_datetime_type(database_in_list)

# remove canceled operations
database_executed = delete_canceled_operations(database_formatted)

# sort all database by date
database_sorted = sort_database_by_date(database_executed)

# get the 5 last operations
the_last_operations = database_sorted[-5:]

# get statistics for each operation
for operation in the_last_operations:
    print(operation['date'].strftime("%d.%m.%Y") + ' ' + operation['description'])
    #print(operation['from'] + ' -> ' + operation['to'])
    print(operation['operationAmount']['amount'] + ' ' + operation['operationAmount']['currency']['name'] + "\n")
