# Simple HTTP Server

## Description
This project features a simple HTTP server written in Python that serves static files from a designated directory. This setup is ideal for hosting simple websites or frontend applications directly from your local machine or within a Docker container.

## Project Structure
### main.py # Main Python script for the HTTP server
### requirements.txt # List of dependencies (empty for this project)
### Dockerfile # Instructions for building the Docker container
### web # Directory for static files like HTML, CSS, etc.
### index.html # Example HTML file to be served

## Build and Run with Docker
### Build the Docker image:
```bash
docker build -t simple-http-server .
```
### Run the container:
From the project directory, run:
```bash
docker run -p 8000:8000 simple-http-server
```

### Access the server at http://localhost:8000.
