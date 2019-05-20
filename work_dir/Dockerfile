FROM python:3
MAINTAINER yumemo

WORKDIR /root

ENV HOSTNAME localhost
ADD requirements.in /root/requirements.in

RUN echo "export PS1='[\u@\h \W]# '" >> /etc/profile
RUN apt-get update

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pip-tools
RUN pip-compile /root/requirements.in
RUN pip-sync
