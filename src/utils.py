import json


def get_database(path_to_file):
    """
    Get database from a json-file
    :param path_to_file: path to json-file with data
    :return: database in list-type
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        database = json.load(file)
    return database
