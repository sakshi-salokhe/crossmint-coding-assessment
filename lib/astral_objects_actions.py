from utils.api_calls import handle_get_api_call
from utils.helpers import retrieve_value_from_env


class AstralObjectsActions:
    def __init__(self):
        self.base_url = retrieve_value_from_env("BASE_URL") + '/api'

        self.candidate_id = retrieve_value_from_env("CANDIDATE_ID")

        self.params = {
            'candidateId': self.candidate_id
        }

    def get_goal_map(self):
        url = f"{self.base_url}/map/{self.candidate_id}/goal"
        goal_map_response = handle_get_api_call(url)
        
        return goal_map_response['goal'] if goal_map_response is not None else None
