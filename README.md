# Raspberry Pi Temperature Server using Docker Compose

This project uses `docker-compose` to run a multi-container application which checks the 
Raspberry Pi's CPU temperature and provides the result through a very simple AJAX web
application. It is intentionally more complicated than necessary to show how 
`docker-compose` can be used to deploy applications on the Raspberry Pi.

The application consists of three containers. The current temperature is read from one
container using Python and then stored in another container using Redis. The value is 
then read from Redis and server over HTTP using NodeJS/Express.

Running docker-compose up will:

1. (If needed) download a Raspbian base docker image.
1. (If needed) download Redis and compile from source inside the redis-rpi image.
1. (If needed) install NodeJS and Python inside the nodejs-rpi and python3-rpi images respectively.
1. Start containers for each image and network them together.
1. Make the NodeJS application available on port 80 (default web port) of the raspberry pi. 

## Initial Setup

Before running this project you will need to install docker and docker-compose on your pi. 
This can be achieved by running the following commands on from a terminal on the Raspberry
pi:

```bash
# Install docker via not-very-secure pipe from curl to shell
curl -sSL https://get.docker.com | sh
    
# Easiest way to install docker-compose is through python's pip
# package manager
pip install docker-compose
```

Once you've installed docker and docker-compose, reboot your pi by running:

```bash
sudo reboot
```

## Running Temperature Server

Once docker and docker-compose are both happily working, simply run:

```bash
# Clone this git repository
git clone https://github.com/tomnewport/rpi-docker-cpu-server.git

# Change to the main directory
cd rpi-docker-cpu-server

# Run docker-compose in detached mode - this may take some time to 
# download and build docker images on first run.
docker-compose up -d
```
