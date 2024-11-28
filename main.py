from lib.astral_objects_actions import AstralObjectsActions


def main():
    astral_objects_client = AstralObjectsActions()
    goal_map = astral_objects_client.get_goal_map()
    print(goal_map)


if __name__ == "__main__":
    main()
