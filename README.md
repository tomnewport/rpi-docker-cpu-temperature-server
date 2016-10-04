# Raspberry Pi Temperature Server using Docker Compose

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
