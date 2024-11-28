import time


def create_megaverse(api_client, goal_map):
    """
    Referring to the gap_map sent as a parameter, makes correct API POST calls
    Sends the correct row and column based on the current cell of the goal map to the POST API Call
    For every API call, waits for the call to finish

    The parameters for the API POST calls for POLYANET, SOLOON and COMETH are the row and column of current cell
    In case of SOLOON, retrieves the color from the goal map for current soloon and sends that additional parameter
    In case of COMETH, retrieves the direction from the goal map for current soloon and sends that additional parameter

    :param api_client:
    :param goal_map:
    :return:
    """
    count_of_astral_objects = 0
    total_rows = len(goal_map)
    total_columns = len(goal_map[0])

    my_megaverse = [[0 for _ in range(total_columns)] for _ in range(total_rows)]

    for row in range(total_rows):
        for column in range(total_columns):
            current_cell_value = goal_map[row][column]

            if current_cell_value != 'SPACE':
                count_of_astral_objects += 1
                params = {
                    'row': row,
                    'column': column
                }
                if current_cell_value == 'POLYANET':
                    api_client.handle_post_api_call('polyanets', params)
                elif 'SOLOON' in current_cell_value:
                    params['color'] = current_cell_value.split('_')[0].lower()
                    api_client.handle_post_api_call('soloons', params)
                elif 'COMETH' in current_cell_value:
                    params['direction'] = current_cell_value.split('_')[0].lower()
                    api_client.handle_post_api_call('comeths', params)
                time.sleep(0.75)

            my_megaverse[row][column] = current_cell_value

    print(f"Completed adding {count_of_astral_objects} astral objects to megaverse.")
