FROM python:3.8.0-alpine3.10
LABEL Maintainer="ymmmtym"

ENV HOSTNAME="keywoo" \
    FLASK_APP="/app/run.py" \
    APP="/app" \
    PS1="[\u@\h \W]# "
COPY ["requirements.txt", "/tmp"]
COPY ["app", "${APP}"]

RUN apk update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt

WORKDIR ${APP}
CMD flask run -h 0.0.0.0
