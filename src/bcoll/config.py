import platformdirs
import os

def exists():
    if platformdirs.user_config_path("bcoll").exists():
        return True
    else:
        return False

def create():
    config = platformdirs.user_config_path("bcoll")
    config.mkdir(parents=True, exist_ok=True)
    cfg = config / "settings.toml"

