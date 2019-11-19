FROM python:3
LABEL maintainer "ymmmtym"
ENV HOSTNAME="keywoo-container" \
    FLASK_APP="/app/run.py" \
    APP_PATH="/app" \
    PS1="[\u@\h \W]# "
ADD ["requirements.in", "/tmp"]
ADD ["app", "$APP_PATH"]
WORKDIR /tmp
RUN apt-get -y update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt
WORKDIR $APP_PATH
CMD flask run -h 0.0.0.0
