""" Module to work with Twitter API friends/list endpoint """

import json


def read_json(file):
    '''
    Reads Twitter API json and returns a dictionary
    '''

    with open(file, mode='r', encoding='utf-8') as f:
        json_file = json.load(f)
    return json_file


def work_json(friends: dict) -> list:
    '''
    Returns a list of friends and their locations
    '''

    locations = []
    for user in friends['users']:
        if not user['location']:
            continue
        else:
            locations.append([user['name'], user['location']])
    return locations
