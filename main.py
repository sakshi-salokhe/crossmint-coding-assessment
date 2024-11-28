from lib.create_metaverse import CreateMetaverseClient
from utils.api_client import ApiClient


def main():
    api_client = ApiClient()

    goal_map = api_client.get_goal_map()

    if goal_map is not None:
        create_metaverse_client = CreateMetaverseClient(api_client, goal_map)
        return create_metaverse_client.create_metaverse()
        # print(resp)
        # print(resp == goal_map)
    else:
        print(f"Goal map does not exist. No metaverse created.")


if __name__ == "__main__":
    main()
