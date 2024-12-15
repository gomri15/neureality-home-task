# neureality-home-task

# Dockerized Application Test Framework

## Application

This repository contains a Flask application with two REST endpoints:
- `/reverse`: Reverses the words in the input string.
- `/restore`: Returns the last reversed string.

## Getting Started

### Build and Run the Docker Container
1. Build the Docker image:
   ```bash
   docker build -t flask-app-test .
