FROM python:3.10-alpine

WORKDIR /usr

ADD . ./app

RUN apk update && apk upgrade

# Needed to install python packages, which needs to be compiled
RUN apk add build-base

RUN pip install --upgrade pip

RUN pip install -r ./app/requirements.txt

EXPOSE 5000