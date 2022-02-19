FROM python:3.8-slim

ARG WORKSPACE=/project

WORKDIR $WORKSPACE

COPY requirements.txt $WORKSPACE/requirements.txt

RUN pip install -r requirements.txt
COPY . $WORKSPACE

CMD python ./manage.py collectstatic

CMD uvicorn helio.asgi:application --host 0.0.0.0 --port 8011 --log-config log.ini
