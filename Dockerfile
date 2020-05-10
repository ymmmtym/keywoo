FROM python:3.8.0-alpine3.10
LABEL Maintainer="ymmmtym"

ENV HOSTNAME="keywoo" \
    APP="/opt/keywoo" \
    PS1="[\u@\h \W]# "
ENV FLASK_APP="${APP}/run.py"
COPY [".", "${APP}"]

WORKDIR ${APP}
RUN apk update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt

EXPOSE 5000
CMD flask run -h 0.0.0.0