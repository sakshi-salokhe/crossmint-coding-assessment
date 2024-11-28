import requests
import json

from utils.helpers import retrieve_value_from_env


class ApiClient:
    """
    API Client

    Retrieves the base URL and candidate ID from env
    Contains methods to handle API calls and raise exceptions
    """

    def __init__(self):
        self.base_api_url = retrieve_value_from_env("BASE_URL") + '/api'

        self.candidate_id = retrieve_value_from_env("CANDIDATE_ID")

    def handle_post_api_call(self, url_suffix, params):
        """
        Makes a POST request to the given URL Suffix
        Attaches the candidateId value to the parameters being sent

        Params is a dictionary containing Key-Value pairs of the request payload
        Ex. if url_suffix is polyanets, url will be https://<base_url>/api/polyanets
        Raises exceptions if the endpoint call failed.

        :param url_suffix:
        :param params:
        :return:
        """
        params['candidateId'] = self.candidate_id
        post_url = f"{self.base_api_url}/{url_suffix}"
        try:
            response = requests.post(post_url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions as error:
            print(f'Post call for {url_suffix} failed with error: {str(error)}')
            raise error from None

    def handle_delete_api_call(self, url_suffix, params):
        """
        Makes a DELETE request to the given URL Suffix
        Attaches the candidateId value to the parameters being sent

        Params is a dictionary containing Key-Value pairs of the request payload for the item to delete
        Ex. if url_suffix is polyanets, url will be https://<base_url>/api/polyanets
        Raises exceptions if the endpoint call failed.

        :param url_suffix:
        :param params:
        :return:
        """
        params['candidateId'] = self.candidate_id

        delete_url = f"{self.base_api_url}/{url_suffix}"
        headers = {'content-type': 'application/json'}

        try:
            response = requests.delete(delete_url, data=json.dumps(params), headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions as error:
            print(f'Delete call for {url_suffix} failed with error: {str(error)}')
            raise error

    def get_goal_map(self):
        """
        Calls the Map Goal endpoint to retrieve the JSON containing the goal matrix

        :return:
        """
        try:
            get_goal_map_url = f"{self.base_api_url}/map/{self.candidate_id}/goal"
            goal_map_response = requests.get(get_goal_map_url)
            return goal_map_response.json().get('goal')
        except requests.exceptions as error:
            print(f'Get call for get_goal_map failed with error: {str(error)}')
            raise error
