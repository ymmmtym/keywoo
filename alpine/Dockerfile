FROM python:3-alpine
MAINTAINER yumemo
WORKDIR /root
ENV HOSTNAME="flask-container" \
    PS1="[\u@\h \W]# "
ADD requirements.txt /root/requirements.txt
RUN apk update
RUN apk add --no-cache --update libffi-dev build-base
RUN apk --update-cache \
    add musl \
    linux-headers \
    gcc \
    g++ \
    make \
    gfortran \
    openblas-dev
RUN pip install --upgrade pip && \
   pip install --upgrade setuptools && \
   pip install numpy flake8 scipy mscikit-learn requests beautifulsoup4 Flask && \
   pip install pandas atplotlib --no-build-isolation

# issue
# wrong with hang caused installing library → pandas matplotlib
