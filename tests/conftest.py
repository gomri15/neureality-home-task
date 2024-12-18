# test_app.py
import pytest

from src.common.utils import wait_for_server
from src.config.config_models import NeuRealityAutomationConfig
from src.neu_reality import NeuReality


@pytest.fixture(scope="session", autouse=True)
def neureality():
    """
    Initialize NeuReality with the configuration and provide it as a fixture.
    Manages Docker container lifecycle during the test session.
    """
    config = NeuRealityAutomationConfig.from_json()
    neureality = NeuReality(config)

    try:
        if config.build_docker:
            neureality.docker_manager.build_image()
            neureality.docker_manager.run_container()
            wait_for_server(config.api_base_url)
        
        neureality.docker_manager.wait_for_container_to_start()
        yield neureality
    finally:
        neureality.docker_manager.stop_container()
