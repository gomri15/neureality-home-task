
# **Flask Application and Test Framework**

## **Overview**
This project includes:
1. A **Python Flask REST API** with two endpoints:
   - `/reverse`: Receives a string and returns the words in reverse order.
   - `/restore`: Returns the last result from the `/reverse` endpoint.
2. A **pytest-based testing framework** that:
   - Starts the Docker container.
   - Tests both endpoints for correctness.

---

## **Prerequisites**

Before you begin, ensure the following tools are installed:

- **Docker**: To containerize and run the Flask application.
- **Python 3.x**: Required for pytest and additional testing dependencies.

It is recommended to use a virtual environment:
```bash
python -m venv dev
```
A new `dev` directory should be created in the project directory.

- To activate on Windows:
  ```powershell
  dev\Scripts\activate
  ```

- To activate on Linux/Mac:
  ```bash
  source dev/bin/activate
  ```

Install required Python dependencies:
```bash
pip install -r requirements.txt
```

---

## **Modes of Running the Automation**

This automation supports **two modes**:

### **Mode 1: Build and Run the Docker Container Automatically**
In this mode, the automation handles:
- Building the Docker image.
- Starting the Docker container.
- Running the tests.

This is the default behavior and requires no manual Docker setup. The `config.json` file must have the default `docker_image` and `docker_container` configurations.

### **Mode 2: Use a Preexisting Docker Container**
This mode assumes:
- You have already built the Docker image.
- You have started the container manually.
  
The `config.json` file must be updated with the existing container's configurations (e.g., `docker_image`, `docker_container`, and `docker_port`).

---

## **Configuration**

The project reads its configuration from `config.json`. Modify this file as needed:

```json
{
  "docker_image": "flask-app-test",
  "docker_container": "flask-app-test-container",
  "docker_port": 5000,
  "api_base_url": "http://localhost:5000",
  "container_start_wait_time": 5
}
```

**Key Fields:**
- `docker_image`: Name of the Docker image.
- `docker_container`: Name of the Docker container.
- `docker_port`: Port on which the application runs.
- `api_base_url`: Base URL of the application (e.g., `http://localhost:5000`).
- `container_start_wait_time`: Time to wait for the container to start (default: 5 seconds).

---

## **1. Running in Build-and-Run Mode (Mode 1)**

Simply run the tests without any prior Docker setup:
```bash
pytest
```

This will:
1. Build the Docker image.
2. Start the Docker container.
3. Wait for the container to be ready.
4. Run the test suite.
5. Stop the container after the tests.

---

## **2. Running in Preexisting-Container Mode (Mode 2)**

Follow these steps to use an existing Docker setup:

### **Step 1: Build the Docker Image (if not already built)**
```bash
docker build -t flask-app-test .
```

### **Step 2: Start the Docker Container**
```bash
docker run -d --rm --name flask-app-container -p 5000:5000 flask-app-test
```

### **Step 3: Update the Configuration**
Ensure `config.json` matches the preexisting container settings:
```json
{
  "docker_image": "flask-app-test",
  "docker_container": "flask-app-container",
  "docker_port": 5000,
  "api_base_url": "http://localhost:5000",
  "container_start_wait_time": 0
}
```

### **Step 4: Run the Tests**
Run the tests as usual:
```bash
pytest
```

---

## **3. Verifying the Application**

You can manually test the application using `curl` or a browser:

### Test the `/reverse` Endpoint
```bash
curl "http://localhost:5000/reverse?in=The quick brown fox"
```
**Response**:
```json
{"result": "fox brown quick The"}
```

### Test the `/restore` Endpoint
```bash
curl "http://localhost:5000/restore"
```
**Response**:
```json
{"result": "fox brown quick The"}
```

---

## **4. Understanding Successful Test Results**

### **Successful Test Run**:
- All tests pass without errors.
- Sample pytest output:
   ```plaintext
   ============================= test session starts =============================
   platform linux -- Python 3.x, pytest-x.x.x, ...
   collected 2 items

   test_app.py ..                                                            [100%]

   ============================== 2 passed in 1.23s ==============================
   ```

---

## **5. Stopping the Container**

To manually stop the running container:
```bash
docker stop flask-app-container
```

---

## **References**

- [Docker Documentation](https://docs.docker.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
