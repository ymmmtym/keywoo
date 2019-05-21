FROM python:3
MAINTAINER yumemo
WORKDIR /root
ENV HOSTNAME="work-container" \
    PS1='[\u@\h \W]# '
ADD requirements.in /root/requirements.in
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pip-tools && \
    pip-compile /root/requirements.in && \
    pip-sync
