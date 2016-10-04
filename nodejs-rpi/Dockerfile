FROM sdhibit/rpi-raspbian:latest

RUN apt update

RUN apt install -y wget

WORKDIR /tmp/

RUN wget -q -O - https://deb.nodesource.com/setup_6.x | bash

RUN apt update

RUN apt install -y nodejs

EXPOSE 3000

WORKDIR /etc/
