from lib.create_megaverse import CreatemegaverseClient
from utils.api_client import ApiClient


def main():
    api_client = ApiClient()

    goal_map = api_client.get_goal_map()

    if goal_map is not None:
        create_megaverse_client = CreatemegaverseClient(api_client, goal_map)
        return create_megaverse_client.create_megaverse()
    else:
        print(f"Goal map does not exist. No megaverse created.")


if __name__ == "__main__":
    main()
