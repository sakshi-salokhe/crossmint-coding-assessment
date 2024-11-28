import time


class CreateMegaverseClient:
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
                    elif 'SOLOON' in current_cell_value:
                        params['color'] = current_cell_value.split('_')[0].lower()
                        self.api_client.handle_post_api_call('soloons', params)
                    elif 'COMETH' in current_cell_value:
                        params['direction'] = current_cell_value.split('_')[0].lower()
                        self.api_client.handle_post_api_call('comeths', params)
                    time.sleep(1)

        print("Matches goal: ", result_megaverse == self.goal_map)
