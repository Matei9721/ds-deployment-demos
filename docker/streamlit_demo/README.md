# Docker & Streamlit Application Demo

This demo shows how easy it is to deploy a Streamlit Application using Docker. This Streamlit application contains 
multiple pages which show what different functionalities one could implement with this set-up (serving a model, creating
a chatbot, or visualizing data).

The current code has been already containerized and pushed to Docker hub at 
https://hub.docker.com/r/matei9721/docker-streamlit-ds-demo/tags. To get started with this demo, the first step would be
to try and pull and image and run it locally. We can begin by pulling the image:

`docker pull matei9721/docker-streamlit-ds-demo:latest`

This can take a bit as the uncompressed image size is ~6 GB. We can check if we pulled the image sucesfully by running

`docker image ls` and checking for the image tag.

Once we have the image, we can run it using the command:

`docker run -p 8501:8501 matei9721/docker-streamlit-ds-demo:latest`

In the command above, we tell docker to run the image with the tag **matei9721/docker-streamlit-ds-demo:latest** while 
opening the port 8501 both internally and externally. We need this port open, because this is the default port on which 
Streamlit is running. We can select any other external ports, but the internal port is being set when we create the application
and the Dockerfile.

