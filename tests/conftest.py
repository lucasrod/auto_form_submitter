import pytest
from utils.env_loader import load_environment

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_environment()