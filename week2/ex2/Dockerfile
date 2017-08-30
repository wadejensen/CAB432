############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################
# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Wade Jensen

# Install basic applications, Python, Python tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    dialog \
    git \
    net-tools \
    python \
    python-dev \
    python-setuptools \
    python-distribute \
    python-pip \
    tar \
    wget

# Get pip to download and install Python requirements:
RUN pip install flask
RUN pip install cherrypy

# Copy the application folder inside the container
ADD /app /app

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /app

# Set the default command to execute when creating a new container
# i.e. using CherryPy to serve the application
CMD python server.py


