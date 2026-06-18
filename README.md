# API-base

## Objective
Baseline infrastructure designed to serve as a scalable, containerized delivery mechanism for future machine learning model deployments.

## Technology Stack
* **Language:** Python 3.13
* **Serving Layer:** FastAPI
* **Server:** Uvicorn
* **Containerization:** Docker

## Local Deployment Protocol

### 1. Build the Image
Execute the following command in the root directory to compile the Docker image:
`docker build -t api_base .`

### 2. Run the Container
Execute the following command to instantiate the container, run it in the background, and bind the internal port to your local machine:
`docker run -d -p 8000:8000 --name api_instance api_base`

### 3. Verify Infrastructure
Navigate strictly to `http://localhost:8000/docs` in your browser to access the live Swagger UI dashboard and verify the baseline endpoint.
