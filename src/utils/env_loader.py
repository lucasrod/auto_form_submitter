import os
from dotenv import load_dotenv

def load_environment():
    # Prioridad: variable de sistema ENV o .env fallback
    env_type = os.getenv("ENVIRONMENT")  # ya puede venir desde el sistema
    if not env_type:
        # fallback: cargar una .env base que defina ENVIRONMENT
        base_env = os.path.abspath("config/.env")
        load_dotenv(dotenv_path=base_env)
        env_type = os.getenv("ENVIRONMENT", "TESTING")

    # Ahora cargamos el .env correspondiente según ENVIRONMENT
    env_file = f".env.{env_type.lower()}"
    env_path = os.path.abspath(os.path.join("config", env_file))

    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path, override=True)
    else:
        raise FileNotFoundError(f"Environment file '{env_file}' not found in config/")
