import logging
import os

from dotenv import load_dotenv

from utils.exceptions import NoEnvironmentFound


def read_environ():
    # data def
    path = os.path.join(os.getcwd(), "assets")
    # execution
    responses_json = [f for f in os.listdir(path=path) if ".env" in f]
    env_file = responses_json[0]
    if env_file is None:
        raise NoEnvironmentFound
    load_dotenv(os.path.join(path, env_file))
    logging.debug(f"SQLITE_PATH = {os.getenv('SQLITE_PATH')}")
    return None
