FROM python:3
USER root
WORKDIR /root
ENV HOSTNAME="keywoo-container" \
    PS1="[\u@\h \W]# "
ADD ["requirements.in", "/root/requirements.in"]
ADD ["app", "/root/app"]
RUN apt-get -y update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pip-tools && \
    pip-compile /root/requirements.in && \
    pip-sync