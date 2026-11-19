from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "configs" / "base.yaml"


def load_config(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    """Load project configuration from a YAML file."""
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Configuration must contain a YAML mapping.")

    return config
