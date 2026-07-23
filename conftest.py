import pytest
from utils.data_reader import read_json

@pytest.fixture(scope="session")
def base_url():
    config = read_json("config.json")
    return config["base_url"]
