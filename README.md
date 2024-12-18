
# **Flask Application and Test Framework**

## **Overview**
This project includes:
1. A **Python Flask REST API** with two endpoints:
   - `/reverse`: Receives a string and returns the words in reverse order.
   - `/restore`: Returns the last result from the `/reverse` endpoint.
2. A **pytest-based testing framework** that:
   - Starts the Docker container.
   - Tests both endpoints for correctness.
   - Generates test results in JUnit XML format.

---

## **Prerequisites**

Before you begin, ensure the following tools are installed:

- **Docker**: To containerize and run the Flask application.
- **Python 3.x**: Required for pytest and additional testing dependencies.

   It is recommended you use a virtual env
   ```bash
   pip install venv
   python -m venv dev
   ```
   A new dev directory should be created in the project
   Using windows
   ```powershall
   dev/scripts/activate
   ```
   using Linux

   ```bash
   source dev/scripts/activate
   ```

Install requirements

```bash
pip install -r requirements.txt
```

---

## **1. Building the Docker Container**

To build the Docker container for the application:

**Note**: The automation project already does this for you if you are ok with that and the default settings it uses feel free to skip this part.

1. Open your terminal and navigate to the project directory (where `Dockerfile` is located).

2. Run the following command to build the Docker image:
   ```bash
   docker build -t flask-app-test .
   ```
   - `-t flask-app-test`: Tags the image with the name `flask-app-test`.

3. Verify the image was created successfully:
   ```bash
   docker images
   ```
   - You should see `flask-app-test` listed.

---

## **2. Running the Application Container**

Run the application using the following command:
```bash
docker run -d --rm --name flask-app-container -p 5000:5000 flask-app-test
```

### Explanation:
- `-d`: Runs the container in detached mode (background).
- `--rm`: Removes the container after stopping it.
- `--name flask-app-container`: Assigns a name to the container.
- `-p 5000:5000`: Maps port 5000 on the host to port 5000 in the container.

### Verifying the Application:
To check if the application is running, open a browser or use `curl`:

1. **Test `/reverse` Endpoint**:
   ```bash
   curl "http://localhost:5000/reverse?in=The quick brown fox"
   ```
   **Response**:
   ```json
   {"result": "fox brown quick The"}
   ```

2. **Test `/restore` Endpoint**:
   ```bash
   curl "http://localhost:5000/restore"
   ```
   **Response**:
   ```json
   {"result": "fox brown quick The"}
   ```

---

## **3. Running Tests**

The project includes a pytest-based test framework in `test_app.py` to validate the application.

### **Steps to Run Tests**:
1. Ensure the Docker container is not already running. If it is, stop it:
   ```bash
   docker stop flask-app-container
   ```

2. Run the tests using the following command:
   ```bash
   pytest --junitxml=report.xml
   ```

### **Explanation**:
- `pytest`: Runs the test suite.
- `--junitxml=report.xml`: Generates a JUnit-compatible test report in `report.xml`.

---

## **4. Understanding Successful Test Results**

### **Successful Test Run**:
- All tests pass without errors.
- Sample output in the terminal:
   ```plaintext
   ============================= test session starts =============================
   platform linux -- Python 3.x, pytest-x.x.x, ...
   collected 2 items

   test_app.py ..                                                            [100%]

   ============================== 2 passed in 1.23s ==============================
   ```

- A **JUnit XML report** is generated as `report.xml`:
   ```xml
   <testsuite name="pytest" tests="2" failures="0">
       <testcase classname="test_app" name="test_reverse_endpoint" time="0.5"/>
       <testcase classname="test_app" name="test_restore_endpoint" time="0.7"/>
   </testsuite>
   ```

### **Failed Tests**:
If any test fails, pytest displays the failure reason. For example:
```plaintext
=================================== FAILURES ===================================
______________________________ test_reverse_endpoint ____________________________

AssertionError: assert 'fox brown' == 'brown fox'
```
- Fix the issues in the code or the test suite and rerun pytest.

---

## **5. Stopping the Container**

To stop the running container:
```bash
docker stop flask-app-container
```

---

## **6. Summary**

### **Steps to Build, Run, and Test**:
1. **Build** the Docker image:
   ```bash
   docker build -t flask-app-test .
   ```

2. **Run** the container:
   ```bash
   docker run -d --rm --name flask-app-container -p 5000:5000 flask-app-test
   ```

3. **Run Tests**:
   ```bash
   pytest --junitxml=report.xml
   ```

4. **Stop** the container:
   ```bash
   docker stop flask-app-container
   ```

### **Successful Test Outcome**:
- All tests pass.
- The `report.xml` file contains the results.

---

## **References**

- [Docker Documentation](https://docs.docker.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
