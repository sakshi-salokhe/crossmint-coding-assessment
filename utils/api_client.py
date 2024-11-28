import requests
import json
from utils.helpers import retrieve_value_from_env


class ApiClient:
    def __init__(self):
        self.base_api_url = retrieve_value_from_env("BASE_URL") + '/api'

        self.candidate_id = retrieve_value_from_env("CANDIDATE_ID")

    def handle_post_api_call(self, url_suffix, params):
        params['candidateId'] = self.candidate_id

        post_url = f"{self.base_api_url}/{url_suffix}"
        try:
            response = requests.post(post_url, json=params)
            return response.json()
        except requests.exceptions as error:
            print(f'Post call for {url_suffix} failed with error: {str(error)}')
            raise error

    def handle_delete_api_call(self, url_suffix, params):
        params['candidateId'] = self.candidate_id
        
        delete_url = f"{self.base_api_url}/{url_suffix}"
        headers = {'content-type': 'application/json'}

        try:
            response = requests.delete(delete_url, data=json.dumps(params), headers=headers)
            return response.json()
        except requests.exceptions as error:
            print(f'Delete call for {url_suffix} failed with error: {str(error)}')
            raise error

    def get_goal_map(self):
        try:
            get_goal_map_url = f"{self.base_api_url}/map/{self.candidate_id}/goal"
            goal_map_response = requests.get(get_goal_map_url)
            return goal_map_response.json().get('goal')
        except requests.exceptions as error:
            print(f'Get call for get_goal_map failed with error: {str(error)}')
            raise error
