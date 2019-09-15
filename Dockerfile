FROM python:3
MAINTAINER ymmmtym
ENV HOSTNAME="keywoo-container" \
    FLASK_APP="/keywoo/app/run.py" \
    PS1="[\u@\h \W]# "
ADD ["requirements.in", "/tmp"]
ADD ["app", "/keywoo/app"]
WORKDIR /tmp
RUN apt-get -y update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pip-tools && \
    pip-compile /tmp/requirements.in && \
    pip-sync
WORKDIR /keywoo/app
CMD flask run -h 0.0.0.0 -p $PORT
