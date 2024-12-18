import requests

from src.common.dependencies import Dependencies
from src.config.config_models import NeuRealityAutomationConfig


class StringHandlerApiClient:
    def __init__(self, config: NeuRealityAutomationConfig, dependencies: Dependencies):
        self.config = config
        self.dependencies = Dependencies()
        self.base_url = config.api_base_url

    def reverse(self, input_string):
        response = requests.get(
            f"{self.base_url}/reverse", params={"in": input_string})
        response.raise_for_status()
        return response.json()

    def restore(self):
        response = requests.get(f"{self.base_url}/restore")
        response.raise_for_status()
        return response.json()
