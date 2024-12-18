

from src.api_client.string_handler_api_client import StringHandlerApiClient
from src.common.docker_manager import DockerManager
from src.common.dependencies import Dependencies


class NeuReality:
    def __init__(self, config):
        """
        Parent class to manage Docker and API interactions.
        Initializes DockerManager and Route with the provided configuration.
        """
        self.config = config
        self.dependencies = Dependencies()
        self.docker_manager = DockerManager(config, self.dependencies)
        self.string_handler_api_client = StringHandlerApiClient(config, self.dependencies)
