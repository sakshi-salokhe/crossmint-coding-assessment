import os
from dotenv import load_dotenv

load_dotenv()


def retrieve_value_from_env(env_key):
    try:
        return os.getenv(env_key)
    except ValueError as error:
        print(f'Fetching Base URL from env failed for key: {env_key} with error: {str(error)}')
        raise error
