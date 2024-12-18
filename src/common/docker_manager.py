import subprocess
import time

from src.common.dependencies import Dependencies
from src.config.config_models import NeuRealityAutomationConfig


class DockerManager:
    def __init__(self, config: NeuRealityAutomationConfig, dependencies: Dependencies):
        self.dependencies = dependencies
        self.config = config

    def build_image(self):
        subprocess.run(
            ["docker", "build", "-t", self.config.docker_image, "webserver/."],
            check=True,
        )

    def run_container(self):
        subprocess.run(
            [
                "docker", "run", "-d", "--rm",
                "--name", self.config.docker_container,
                "-p", f"{self.config.docker_port}:{self.config.docker_port}",
                self.config.docker_image,
            ],
            check=True,
        )

    def stop_container(self):
        subprocess.run(
            ["docker", "stop", self.config.docker_container], check=True)

    def is_container_running(self):
        result = subprocess.run(
            ["docker", "ps", "--filter",
                f"name={self.config.docker_container}", "--format", "{{.Names}}"],
            capture_output=True, text=True
        )
        self.dependencies.logger.info(f"Container status is {result.stdout}")
        return self.config.docker_container in result.stdout

    def wait_for_container_to_start(self, timeout=None):
        timeout = timeout or self.config.container_start_wait_time
        elapsed_time = 0
        interval = 1  # Check every second
        while elapsed_time < timeout:
            if self.is_container_running():
                return True
            time.sleep(interval)
            elapsed_time += interval
        raise TimeoutError(
            f"Container {self.config.docker_container} did not start within {timeout} seconds.")
