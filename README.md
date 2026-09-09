# CloudLab — Flask & MySQL DevOps Project

A containerized two-tier web application built with **Python Flask and MySQL**, using Docker Compose to manage the application and database services.

This project is part of my practical Cloud and DevOps learning journey, where I am applying containerization, Linux, Git, networking, and CI/CD concepts to a real application.

## Project Overview

CloudLab is a simple web application that allows users to submit messages through a Flask web interface. Submitted messages are stored in a MySQL database.

The application consists of two main services:

* **Flask Web Application** — Handles the web interface and API requests.
* **MySQL Database** — Stores submitted messages.

The services communicate through a private Docker Compose network.

## Architecture

```text
                  User
                   |
                   v
          +------------------+
          |   Flask Web App  |
          |    Container     |
          +--------+---------+
                   |
                   v
          +------------------+
          |  MySQL Database  |
          |    Container     |
          +------------------+

              Docker Compose
```

## Technologies Used

* Python
* Flask
* MySQL
* Docker
* Docker Compose
* Git & GitHub
* Jenkins
* Linux
* Bash
* HTML
* JavaScript

## Features

* Flask-based web application
* MySQL database integration
* Containerized application environment
* Docker Compose service orchestration
* Persistent MySQL storage using Docker volumes
* Container health checks
* Application health endpoint
* Form submission through JavaScript
* Automated database table creation
* Jenkins pipeline for building and refreshing the application

## Application Endpoints

### Main Application

```text
http://localhost:5000
```

### Health Check

```text
http://localhost:5000/health
```

The health endpoint returns the current application status and can be used for basic deployment verification.

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Emmanuel-Devo/cloudlab-flask-devops.git
```

### 2. Enter the project directory

```bash
cd cloudlab-flask-devops
```

### 3. Build and start the services

```bash
docker compose up -d --build
```

### 4. Check the containers

```bash
docker compose ps
```

Both the Flask application and MySQL database should be running.

### 5. Open the application

Visit:

```text
http://localhost:5000
```

## Useful Docker Commands

Stop the application:

```bash
docker compose down
```

View application logs:

```bash
docker compose logs web
```

View database logs:

```bash
docker compose logs database
```

Restart the services:

```bash
docker compose restart
```

Rebuild the application:

```bash
docker compose up -d --build
```

## CI/CD

The project includes a `Jenkinsfile` for automating the application workflow.

The pipeline is designed around:

```text
GitHub
   |
   v
Jenkins
   |
   v
Docker Image Build
   |
   v
Docker Compose Deployment
   |
   v
Application Verification
```

This provides practical experience with integrating source control, automated builds, containerization, and deployment.

## Project Structure

```text
cloudlab-flask-devops/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
├── message.sql
├── requirement.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── diagrams/
```

## What I Learned

Through this project, I practiced:

* Building a Flask application
* Connecting an application to MySQL
* Creating Docker images
* Running multi-container applications with Docker Compose
* Creating container health checks
* Managing persistent database storage
* Using Git and GitHub for version control
* Writing a Jenkins CI/CD pipeline
* Troubleshooting container and networking issues
* Structuring a practical DevOps project

## Author

**Emmanuel Chima**

Cloud Engineering & DevOps Learner

GitHub:
https://github.com/Emmanuel-Devo
