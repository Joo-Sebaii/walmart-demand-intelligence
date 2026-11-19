from walmart_demand.config import load_config


def test_load_config():
    config = load_config()

    assert config["project"]["name"] == "walmart-demand-intelligence"
    assert config["project"]["random_seed"] == 42
    assert config["logging"]["level"] == "INFO"
