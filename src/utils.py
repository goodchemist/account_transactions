import json
from datetime import datetime


def get_database(path_to_file):
    """
    Get database from a json-file
    :param path_to_file: path to json-file with data
    :return: database in list-type
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        database = json.load(file)
    return database


def change_date_to_datetime_type(lst):
    """
    from the list of dictionaries receives a new list, where the date for operation
    is represented as datetime type. If there isn't data for operation, then the entire
    operation doesn't appear in the new list.
    :param lst: list of dictionaries
    :return: new list of dictionaries, where the date is datetime type
    """
    new_lst = []
    for i in range(0, len(lst)):
        date_str = lst[i].get('date')
        if date_str:
            date_formatted = datetime.fromisoformat(date_str)
            lst[i]['date'] = date_formatted
            new_lst.append(lst[i])
    return new_lst


def sort_database_by_date(database_lst):
    """
    sort database by the key 'date'
    :param database_lst: list of dictionaries
    :return: sorted list of dictionaries by key='date'
    """
    database_sorted = sorted(database_lst, key=lambda x: x['date'])
    return database_sorted


def delete_canceled_operations(database):
    """
    delete canceled operations in database with all operations
    :param database: list of dictionaries
    :return: list of dictionaries with only executed operations
    """
    database_executed = [operation for operation in database if operation['state'] == "EXECUTED"]
    return database_executed


def encode_invoice(invoice):
    """
    encode invoice or card number using '*'
    :param invoice: invoice or card with all digits
    :return: invoice with the last 4 digit or card with first 6 and last 4 digits
    """
    invoice_lst = invoice.split(' ')
    if invoice_lst[0].capitalize() == 'Счет':
        invoice_lst[1] = '**' + invoice_lst[1][-4:]
    else:
        for i in range(1, len(invoice_lst)):
            if invoice_lst[i].isdigit():
                invoice_lst[i] = invoice_lst[i][:4] + ' ' + invoice_lst[i][4:6] + '** **** ' + invoice_lst[i][-4:]
    result = ' '.join(invoice_lst)
    return result
