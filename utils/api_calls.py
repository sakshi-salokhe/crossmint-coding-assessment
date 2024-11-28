import requests
import json


def handle_post_api_call(url, params):
    try:
        response = requests.post(url, json=params)
        return response.json()
    except requests.exceptions as error:
        print(f'Post call for URL {url} failed with error: {str(error)}')
        raise error


def handle_delete_api_call(url, params):
    headers = {'content-type': 'application/json'}

    try:
        response = requests.delete(url, data=json.dumps(params), headers=headers)
        return response.json()
    except requests.exceptions as error:
        print(f'Delete call for URL {url} failed with error: {str(error)}')
        raise error


def handle_get_api_call(url, params=None):
    try:
        response = requests.get(url, params=params)
        return response.json()
    except requests.exceptions as error:
        print(f'Get call for URL {url} failed with error: {str(error)}')
        raise error
