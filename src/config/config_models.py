from pydantic import BaseModel, Field
import json
from pathlib import Path


class NeuRealityAutomationConfig(BaseModel):
    docker_image: str = Field(default="flask-app-test")
    docker_container: str = Field(default="flask-app-test-container")
    docker_port: int = Field(default=5000)
    api_base_url: str = Field(default="http://localhost:5000")
    container_start_wait_time: int = Field(default=5)
    build_docker: bool = Field(default=True)

    @classmethod
    def from_json(cls, config_path: str = "src/config/config.json"):
        """
        Load configuration from a JSON file.
        :param config_path: Path to the JSON config file.
        :return: An instance of AppConfig.
        """
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found at {config_path}")

        with open(config_file, "r") as file:
            config_data = json.load(file)

        return cls(**config_data)
