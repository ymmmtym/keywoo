FROM ghcr.io/astral-sh/uv:0.13.8 AS uv

FROM python:3.11-alpine
LABEL maintainer.label="yumenomatayume"

ENV HOSTNAME="keywoo" \
    APP="/opt/keywoo" \
    PS1="[\u@\h \W]# " \
    UV_PROJECT_ENVIRONMENT="/usr/local" \
    UV_PYTHON_DOWNLOADS="never" \
    UV_LINK_MODE="copy"

COPY --from=uv /uv /uvx /bin/

WORKDIR ${APP}
COPY ["pyproject.toml", "uv.lock", "${APP}/"]

RUN apk update && \
    apk add --no-cache gcc build-base linux-headers postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    uv sync --frozen --no-dev && \
    apk --purge del .build-deps

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY [".", "${APP}"]
ENV FLASK_APP="${APP}/run.py"

EXPOSE 5000
ENTRYPOINT [ "sh", "-c" ]
CMD ["/wait && ${APP}/run.sh"]
