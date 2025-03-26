import os
from dotenv import load_dotenv

def test_env_variables_present():
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/.env"))
    load_dotenv(dotenv_path=dotenv_path)

    required_vars = ["USERNAME", "PASSWORD", "LOGIN_URL"]
    missing = [var for var in required_vars if not os.getenv(var)]
    assert not missing, f"Missing or empty env variables: {', '.join(missing)}"
