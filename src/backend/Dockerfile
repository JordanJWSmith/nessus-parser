FROM python:3.7-alpine

WORKDIR /srv
EXPOSE 8000

RUN apk add --update alpine-sdk

# Copy requirements.txt before code to let Docker cache Python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /srv

ENTRYPOINT python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000

