#!/bin/bash

sudo apt-get docker
sudo curl -fsSL https://get.docker.com/ | sh
sudo usermod -aG docker ubuntu
