import os
from dotenv import load_dotenv

load_dotenv()


def retrieve_value_from_env(env_key):
    """
    Helper method to retrieve value for given Key from ENV if it exists

    :param env_key:
    :return:
    """
    try:
        return os.getenv(env_key)
    except ValueError as error:
        print(f'Fetching Base URL from env failed for key: {env_key} with error: {str(error)}')
        raise error
