"""Configuration constants for the project."""

from os import getenv
from os.path import join, abspath, dirname, exists

import yaml
from easydict import EasyDict

from dotenv import load_dotenv

load_dotenv()


def load_yaml(path: str) -> EasyDict:
    """Load yaml file."""
    with open(path, "r", encoding="utf8") as f:
        config = yaml.safe_load(f)
    return EasyDict(config)


##################################################
# Configurations
##################################################
DEBUG = False
ENV = getenv("ENV", "dev")
RANDOM_STATE = 42


##################################################
# Path
##################################################
ROOT_DIR = abspath(dirname(dirname(__file__)))

CONFIG_DIR = join(ROOT_DIR, "config")
SERVICE_CONFIG_PATH = join(CONFIG_DIR, "service.yaml")


##################################################
# Configurations
##################################################
CFG_SERVICE = load_yaml(SERVICE_CONFIG_PATH)

if __name__ == "__main__":
    print(ENV)
