# test_app.py
import pytest
import requests
import subprocess
import time
from xml.etree.ElementTree import Element, SubElement, tostring

DOCKER_IMAGE = "flask-app-test"
DOCKER_CONTAINER = "flask-app-test-container"


def start_container():
    subprocess.run(["docker", "build", "-t", DOCKER_IMAGE, "webserver/."], check=True)
    subprocess.run([
        "docker", "run", "-d", "--rm", "--name", DOCKER_CONTAINER, "-p", "5000:5000", DOCKER_IMAGE
    ], check=True)
    time.sleep(5)  # Wait for the container to start


def stop_container():
    subprocess.run(["docker", "stop", DOCKER_CONTAINER], check=True)


@pytest.fixture(scope="session", autouse=True)
def docker_container():
    start_container()
    yield
    # stop_container()


def test_reverse_endpoint():
    response = requests.get("http://localhost:5000/reverse",
                            params={"in": "The quick brown fox"})
    assert response.status_code == 200
    assert response.json()["result"] == "fox brown quick The"


def test_restore_endpoint():
    response = requests.get("http://localhost:5000/restore")
    assert response.status_code == 200
    assert response.json()["result"] == "fox brown quick The"


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    results_xml = Element("testsuite")
    for test in session.items:
        testcase = SubElement(results_xml, "testcase", name=test.nodeid)
        if test.outcome == "failed":
            failure = SubElement(testcase, "failure")
            failure.text = "Test failed"
    with open("junit-report.xml", "wb") as f:
        f.write(tostring(results_xml))
