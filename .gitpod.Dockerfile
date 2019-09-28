FROM python:3
ADD ["requirements.in", "/tmp"]
WORKDIR /tmp
RUN apt-get -y update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pip-tools && \
    pip-compile requirements.in && \
    pip-sync
