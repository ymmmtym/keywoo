FROM python:3
MAINTAINER ymmmtym
WORKDIR /root
ENV HOSTNAME="keywoo-container" \
    PS1="[\u@\h \W]# "
ADD ["requirements.in", "/root/requirements.in"]
RUN apt-get -y update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pip-tools && \
    pip-compile /root/requirements.in && \
    pip-sync
ADD ["app", "/root/app"]
WORKDIR /root/app
CMD ["python", "/root/app/run.py"]
