# Docker 101 for Data Science

This will be a short overview of what Docker is, how to install it and how to use it. For more
details I highly advise going direct to the official documentation of Docker which does
an amazing job at explaining basic and complex concepts.

## What is Docker?

Docker is a tool that makes it easier to **create**, **deploy**, and run applications using **containers**. Containers are like
small, lightweight virtual machines that package up all the parts an application needs, such as libraries and other
dependencies, so it can run reliably on any computer. This helps developers ensure that their software works the same
way everywhere, making it easier to develop and manage applications.

In the Data Science context, Docker can help us run our models and applications consistently across different environments
(Linux vs MacOS vs Windows) without having to worry too much about dependencies (all Docker images will run on Linux VMs).

## Installing Docker

You will most likely want to install Docker Desktop (will follow later on what that is) from the official website: 
https://www.docker.com/products/docker-desktop/.

Docker Desktop is supported on Windows, Linux and MacOs.

To check if docker was installed correct, open a terminal and run

`docker --version` Hopefully you should see the version of Docker running on your system.

## Docker Desktop components.

 Docker Desktop is an all-in-one application which includes Docker Engine, Docker CLI, Docker Compose and an User Interface
 which makes easier for beginners to learn and understand what is happening.
 
Docker Engine on the other hand, is the core component of Docker, responsible for running containerized applications. To 
communicate with the engine, we usually use Docker CLI which is a command-line tool that allows users to interact with
the Docker daemon (container manager).

Most of the commands that one would run through the Docker CLI can be done through the Docker Desktop interface making it
a good place to start as it doesn't require memorization of commands :) 

Finally, we have Docker Compose which is a tool for defining and running multi-container Docker applications using a
YAML file. This is for complex application which usually are not the case for DS demos so it's not too important.
## Basic Docker commands (that you should know)

1. The first thing you'll want to do is pull an existing image from a hub. You can achieve that using `docker pull`:

    Example: `docker pull hello-world`

2. Check if you downloaded the image sucesfully by checking all available images using `docker images ls`
3. Once you pulled an image, you will want to run it using `docker run`:

    Example: `docker run hello-world`
    
    - Docker run has many optional flags you can pass. The most important one is to tell Docker which ports to open (to
   communicate with the application). You can do so using the flag *-p*
   
   `docker run -p <host-port>:<container-port> <image-name>`
4. Check if the container is running by listing all containers:

    Example: `docker ps -a`
5. If you've done the step above, you will see each container has an **id**. Using that **id** you can turn off the container
using the command `docker stop <container-id>`
6. If you want to remove a container or image you can use `docker rmi <image-id>` or `docker rm <container-id>`
7. If you want to build your own Docker image (from a Dockerfile which we'll discuss later) you can use the following command
`docker build -t my-app .` where the flag **-t** create a tag (human name) for our image.

## Creating your custom Docker image

Docker can be used just by running the images other people have created, but the strength of Docker is the ease with which 
we can create our own images and share with others. The most important component is the Dockerfile, file which contains 
the instruction that Docker follows to build our image.

Building a simple Dockerfile can take 30 seconds and in most cases is all you will need. Dockerfile configuration
can be optimized for better build quality. Docker documentation has a lot of good information on what a Dockerfile is and
what best practices are:

https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

P.S. If you ever get stuck, ChatGPT is **pretty** good at writing simple Dockerfiles :) 

Once you have created your Dockerfile, build it using (in the same folder as your Dockerfile):

``docker build -t my-app .`` 

From here on you can either run it locally or upload it to the cloud!