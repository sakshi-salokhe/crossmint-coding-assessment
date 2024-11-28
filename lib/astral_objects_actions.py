from utils.api_client import ApiClient


class AstralObjectsActions:
    def __init__(self):
        self.api_client = ApiClient()

    def create_polyanet(self, row, column):
        params = {
            'row': row,
            'column': column
        }

        return self.api_client.handle_post_api_call('polyanets', params)

    def create_soloons(self, row, column, color):
        params = {
            'row': row,
            'column': column,
            'color': color
        }

        return self.api_client.handle_post_api_call('soloons', params)
