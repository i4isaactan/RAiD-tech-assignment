# Task 3 - Containerize Flask Application

## Prerequisites

- Docker is installed
- The files in this repository are downloaded into the same directory

## Files in This Repository

- `Dockerfile`: The Dockerfile used to create the Docker image.
- `exercise.py`: The Flask application. Note: This application listens on port 5252.
- `requirements.txt`: A file listing the Python dependencies.

## Instructions to Build and Run the Docker Container

1. **Build the Docker Image**:
   - Run the following command to build the Docker image:
     ```sh
     docker build -t my-flask-app .
     ```
   - This command will create an image named `my-flask-app`.

2. **Run the Docker Container**:
   - Run the following command to start a container from the `my-flask-app` image and map port 5252 of the container to port 5252 on your host machine:
     ```sh
     docker run -p 5252:5252 my-flask-app
     ```

3. **Access the Application**:
   - Open a web browser and navigate to `http://localhost:5252`. You should see the response from your Flask application.

4. **Health Check**:
   - To access the health check endpoint, add `/healthcheck` to the end of the URL:
     ```
     http://localhost:5252/healthcheck
     ```

