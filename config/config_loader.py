import json
import os


def load_config(env_name: str) -> dict:
    """
    Load the configuration from the environment variable.

    Returns:
    - config: dict
    """
    config_str = os.getenv(env_name)
    if config_str is None:
        raise ValueError(f"Environment variable {env_name} not found.")
    return json.loads(config_str)
