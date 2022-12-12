FROM python:3.9.7-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 channelbot.py
