from lib.create_megaverse import create_megaverse
from utils.api_client import ApiClient
import sys


def handle_megaverse_creation():
    """
    Main method that runs on initialization
    Retrieves the goal map
    Initiates the api client

    Calls the create_megaverse() to create the new megaverse based off of the goal map

    :return:
    """
    goal_map = api_client.get_goal_map()

    if goal_map is not None:
        create_megaverse(api_client, goal_map)
    else:
        print(f"Goal map does not exist. No megaverse created.")


if __name__ == "__main__":
    """
    If the argument for action is delete and contains all arguments, deletes the megaverse object by calling correct endpoint
    Else creates megaverse
    """
    api_client = ApiClient()

    arguments = sys.argv

    action = arguments[1]

    if len(arguments) == 5 and action == 'delete':
        delete_url_suffix = sys.argv[2]
        delete_row = sys.argv[3]
        delete_column = sys.argv[4]

        params = {
            'row': delete_row,
            'column': delete_column
        }

        api_client.handle_delete_api_call(delete_url_suffix, params)
    else:
        handle_megaverse_creation()
