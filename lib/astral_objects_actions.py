class AstralObjectsActions:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_polyanets(self, row, column):
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

    def create_comeths(self, row, column, direction):
        params = {
            'row': row,
            'column': column,
            'direction': direction
        }

        return self.api_client.handle_post_api_call('comeths', params)
