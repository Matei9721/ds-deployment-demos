# Data Science Deployment Demos
This repository contains code examples of different deployment demos for data science POCs from serving models in 
endpoints or containerizing applications.

[docker](docker) - This folder contains all the available demos so far

[docker README file](docker/README.md) - This README file contains all the information you need to get started with Docker 
and the demos in this repository. It's a good place to understand what Docker is, how to run it, and where to use it.

[Streamlit + Docker](docker/streamlit_demo) - It is recommended to start with this demo which gives a nice overview of 
deploying a simple Python application (Streamlit demo) using Docker.

[FastAPI + Docker](docker/fastapi_demo) - This demo shows how we can server a ML model as an REST Endpoint (similar to
SageMaker HTTP endpoints). This docker image can be deployed to an EC2 instance or EKS (Kubernetes).

All the docker images from this repository are uploaded to my private Docker Hub account (see linked folders).
