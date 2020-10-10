FROM python:3.8.0-alpine3.10
LABEL Maintainer="ymmmtym"

ENV HOSTNAME="keywoo" \
    APP="/opt/keywoo" \
    PS1="[\u@\h \W]# "

WORKDIR ${APP}
COPY ["requirements.txt", "${APP}/requirements.txt"]

RUN apk update && \
    apk add --no-cache gcc build-base linux-headers postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install -U pip && \
    pip install -U setuptools && \
    pip install -r requirements.txt --no-cache-dir

RUN apk --purge del .build-deps

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY [".", "${APP}"]
ENV FLASK_APP="${APP}/run.py"

EXPOSE 5000
ENTRYPOINT [ "sh", "-c" ]
CMD ["/wait && ${APP}/run.sh"]