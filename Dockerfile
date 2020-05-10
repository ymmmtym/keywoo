FROM python:3.8.0-alpine3.10
LABEL Maintainer="ymmmtym"

ENV HOSTNAME="keywoo" \
    APP="/opt/keywoo" \
    PS1="[\u@\h \W]# "
ENV FLASK_APP="${APP}/run.py"
COPY [".", "${APP}"]

WORKDIR ${APP}
RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

EXPOSE 5000
CMD /wait && flask run -h 0.0.0.0