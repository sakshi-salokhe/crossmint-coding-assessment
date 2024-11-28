from lib.create_megaverse import create_megaverse
from utils.api_client import ApiClient


def main():
    """
    Main method that runs on initialization
    Retrieves the goal map
    Initiates the api client

    Calls the create_megaverse() to create the new megaverse based off of the goal map

    :return:
    """
    api_client = ApiClient()

    goal_map = api_client.get_goal_map()

    if goal_map is not None:
        create_megaverse(api_client, goal_map)
    else:
        print(f"Goal map does not exist. No megaverse created.")


if __name__ == "__main__":
    main()
