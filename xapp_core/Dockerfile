FROM python:3.7-slim-buster as prod

RUN useradd -rm -d /home/xapp -s /bin/bash -g root -G sudo -u 1000 xapp

USER xapp

RUN mkdir /home/xapp/xapp-core

COPY . /home/xapp/xapp-core

WORKDIR /home/xapp/xapp-core

RUN pip install -r requirements.txt

FROM python:3.7-slim-buster as dev

RUN apt update && apt install sudo -y

RUN useradd -rm -d /home/xapp -s /bin/bash -g root -G sudo -u 1000 xapp

RUN adduser xapp sudo

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER xapp

RUN sudo apt update && sudo apt install -y ssh git vim nano

RUN mkdir /home/xapp/xapp-core

COPY . /home/xapp/xapp-core

WORKDIR /home/xapp/xapp-core

RUN pip install -r requirements.txt
