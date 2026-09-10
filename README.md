# CloudLab Flask DevOps Project

A two-tier Flask and MySQL application containerized with Docker and Docker Compose, with a Jenkins CI/CD pipeline for automated building and deployment.

## Project Overview

This project demonstrates a basic DevOps workflow using GitHub, Jenkins, Docker, Docker Compose, Flask, and MySQL.

The application allows users to submit messages through a web interface. The messages are stored in a MySQL database and remain available after the application is refreshed.

Jenkins is used to automate the process of retrieving the source code, building the Docker image, deploying the application stack, and verifying the deployment.

## Architecture

```text
                         GitHub
                            |
                            v
                         Jenkins
                            |
                 +----------+----------+
                 |                     |
           Checkout Code         Build Docker Image
                 |                     |
                 +----------+----------+
                            |
                            v
                     Docker Compose
                            |
                  +---------+---------+
                  |                   |
                  v                   v
          Flask Application     MySQL Database
             Port 5000             Port 3306
                  |                   |
                  +---------+---------+
                            |
                     Docker Network
                            |
                     Docker Volume
                  (Persistent Storage)
```

## Technologies Used

* Python
* Flask
* MySQL
* Docker
* Docker Compose
* Jenkins
* Git
* GitHub
* HTML
* CSS

## Project Structure

```text
cloudlab-flask-devops/
|
+-- diagrams/
|   +-- Running Docker Containers.JPG
|   +-- Jenkins Success.JPG
|   +-- Docker image build.JPG
|   +-- GitHub checkout.JPG
|   +-- Deployment verification.JPG
|   +-- CloudLab Flask Application Running.JPG
|   +-- Application deployment 1.2.JPG
|   +-- Application deployment 1.1.JPG
|
+-- static/
|   +-- emma.jpg
|
+-- templates/
|   +-- index.html
|
+-- .gitignore
+-- Dockerfile
+-- Jenkinsfile
+-- README.md
+-- app.py
+-- docker-compose.yml
+-- message.sql
+-- requirement.txt
```

## Application

The web application is built with Flask and provides a simple interface for submitting messages.

When a user submits a message:

1. Flask receives the request.
2. The message is validated.
3. Flask connects to MySQL.
4. The message is stored in the `user_messages` table.
5. The application can retrieve and display stored messages.

The application also includes a health endpoint for checking whether the Flask service is responding.

## Database

MySQL is used as the database for the application.

The `user_messages` table contains:

* `message_id` — unique ID for each message
* `content` — the submitted message

The database uses a Docker volume for persistent storage. This allows the stored messages to remain available when the containers are recreated.

## Docker

The application is containerized using Docker.

### Flask Application Container

The Flask application is built using the project `Dockerfile`.

The container:

* Uses Python 3.11
* Installs the required Python dependencies
* Installs the MySQL client dependencies
* Exposes port `5000`
* Runs the Flask application

### MySQL Container

The database uses the official MySQL 8.0 image.

The MySQL container:

* Creates the `devops` database
* Runs on port `3306`
* Uses a persistent Docker volume
* Has a health check
* Communicates with the Flask container through a Docker network

### Docker Network

The Flask and MySQL containers are connected to the same Docker bridge network.

The Flask application connects to the MySQL service using:

```text
database
```

instead of `localhost`.

This allows the two containers to communicate using the Docker Compose service name.

## Docker Compose

Docker Compose is used to manage the Flask and MySQL services.

Build and start the application:

```bash
docker compose up -d --build
```

Check the running services:

```bash
docker compose ps
```

Stop the services:

```bash
docker compose down
```

The database volume is not removed when the containers are stopped normally, allowing the stored data to persist.

## Health Check

The Flask application provides a health endpoint:

```text
http://localhost:5000/health
```

A successful response is:

```json
{
  "status": "healthy"
}
```

The MySQL service also has a Docker health check.

The Flask service is configured to wait for the MySQL database to become healthy before starting.

## Jenkins CI/CD Pipeline

Jenkins is used to automate the build and deployment process.

The pipeline contains four main stages.

### 1. Checkout Source

Jenkins retrieves the project source code from the GitHub repository.

```text
https://github.com/Emmanuel-Devo/cloudlab-flask-devops.git
```

### 2. Create Container Image

Jenkins builds the Flask application into a Docker image:

```text
cloudlab-flask:latest
```

### 3. Refresh Application

Jenkins stops the previous Docker Compose deployment and starts the updated Flask and MySQL services.

The MySQL health check is used to make sure the database is ready before the Flask application starts.

### 4. Verify Deployment

Jenkins checks the Docker Compose services after deployment.

The pipeline completed successfully with:

```text
Finished: SUCCESS
```

## CI/CD Workflow

```text
Developer
    |
    v
  GitHub
    |
    v
 Jenkins
    |
    v
Checkout Source
    |
    v
Build Docker Image
    |
    v
Docker Compose
    |
    +------------------+
    |                  |
    v                  v
  Flask              MySQL
    |                  |
    +--------+---------+
             |
             v
    Deployment Verification
             |
             v
          SUCCESS
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Emmanuel-Devo/cloudlab-flask-devops.git
```

### 2. Enter the project directory

```bash
cd cloudlab-flask-devops
```

### 3. Build and start the containers

```bash
docker compose up -d --build
```

### 4. Check the containers

```bash
docker compose ps
```

### 5. Open the application

Open the following address in your browser:

```text
http://localhost:5000
```

### 6. Test the health endpoint

Open:

```text
http://localhost:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

## Screenshots and Project Evidence

### CloudLab Flask Application Running

The Flask application running successfully in the browser.

![CloudLab Flask Application Running](diagrams/CloudLab%20Flask%20Application%20Running.JPG)

### Running Docker Containers

The Flask and MySQL containers running through Docker.

![Running Docker Containers](diagrams/Running%20Docker%20Containers.JPG)

### GitHub Checkout

Jenkins successfully checking out the project source code from GitHub.

![GitHub Checkout](diagrams/GitHub%20checkout.JPG)

### Docker Image Build

Jenkins successfully building the Flask Docker image.

![Docker Image Build](diagrams/Docker%20image%20build.JPG)

### Application Deployment

Jenkins deploying the Flask application and MySQL database using Docker Compose.

![Application Deployment 1.1](diagrams/Application%20deployment%201.1.JPG)

![Application Deployment 1.2](diagrams/Application%20deployment%201.2.JPG)

### Deployment Verification

Jenkins checking the deployed Docker services.

![Deployment Verification](diagrams/Deployment%20verification.JPG)

### Jenkins Pipeline Success

The completed Jenkins pipeline showing a successful deployment.

![Jenkins Success](diagrams/Jenkins%20Success.JPG)

## Key Features

* Flask web application
* MySQL database integration
* Docker containerization
* Docker Compose multi-container deployment
* Persistent MySQL storage
* Docker bridge networking
* MySQL health check
* Flask health endpoint
* GitHub source-code management
* Jenkins CI/CD pipeline
* Automated Docker image building
* Automated application deployment

## What I Learned

Through this project, I practiced:

* Building a Flask application
* Connecting Flask to MySQL
* Creating Docker images with Dockerfiles
* Running multiple services with Docker Compose
* Connecting containers through Docker networks
* Using Docker volumes for persistent data
* Configuring container health checks
* Using environment variables for application configuration
* Managing source code with Git and GitHub
* Creating Jenkins pipelines
* Automating Docker-based deployments
* Troubleshooting Docker containers and port conflicts
* Understanding a basic CI/CD workflow

## Project Outcome

The project successfully connects GitHub, Jenkins, Docker, Flask, and MySQL into a working CI/CD workflow.

Jenkins retrieves the source code from GitHub, builds the Docker image, deploys the Flask application and MySQL database using Docker Compose, and verifies the deployment.

The Flask application is available locally on port `5000`, while MySQL runs as a separate container with persistent storage.

## Author

**Emmanuel Chukwuere**

Cloud Engineering | DevOps | Networking

GitHub: [Emmanuel-Devo](https://github.com/Emmanuel-Devo)
