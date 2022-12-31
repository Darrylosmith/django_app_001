FROM python:3.9-slim-buster


RUN mkdir -p /code/
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]