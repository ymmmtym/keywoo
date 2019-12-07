FROM python:3.8.0-alpine3.10
LABEL Maintainer "ymmmtym"

ENV HOSTNAME="keywoo-container" \
    FLASK_APP="/app/run.py" \
    APP_PATH="/app" \
    PS1="[\u@\h \W]# "
COPY ["requirements.txt", "/tmp"]
COPY ["app", "$APP_PATH"]

RUN apk update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt

WORKDIR $APP_PATH
CMD flask run -h 0.0.0.0
