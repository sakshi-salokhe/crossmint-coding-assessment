import time


class CreatemegaverseClient:
    def __init__(self, api_client, goal_map):
        self.api_client = api_client
        self.goal_map = goal_map

    def create_megaverse(self):
        total_rows = len(self.goal_map)
        total_columns = len(self.goal_map[0])

        result_megaverse = [[0 for _ in range(total_columns)] for _ in range(total_rows)]

        for row in range(total_rows):
            for column in range(total_columns):
                current_cell_value = self.goal_map[row][column]
                result_megaverse[row][column] = current_cell_value

                if current_cell_value == 'SPACE':
                    continue
                else:
                    params = {
                        'row': row,
                        'column': column
                    }
                    if current_cell_value == 'POLYANET':
                        self.api_client.handle_post_api_call('polyanets', params)
                    elif current_cell_value == 'SOLOON':
                        params['color'] = 'color'  # TODO: Phase 2
                        self.api_client.handle_post_api_call('soloons', params)
                    elif current_cell_value == 'COMETH':
                        params['direction'] = 'direction'  # TODO: Phase 2
                        self.api_client.handle_post_api_call('comeths', params)
                    time.sleep(1)

        return result_megaverse
