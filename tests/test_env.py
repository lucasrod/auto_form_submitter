import os

def test_env_variables_present(load_env):
    required_vars = ["ENVIRONMENT", "USERNAME", "PASSWORD", "GMAIL_USER", "GMAIL_PASS"]
    missing = [var for var in required_vars if not os.getenv(var)]
    assert not missing, f"Missing or empty env variables: {', '.join(missing)}"
