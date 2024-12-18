import requests
from tenacity import retry, wait_fixed, stop_after_delay


@retry(wait=wait_fixed(1), stop=stop_after_delay(30))
def wait_for_server(base_url):
    response = requests.get(f"{base_url}/health")
    response.raise_for_status()
