FROM python:3-alpine3.15

RUN pip3 install flask_restful

ENV PORT_NO=5000
ENV ROOT_DIR=app

COPY . /app
EXPOSE 5000

WORKDIR /app

RUN pip install -r requirements.txt

CMD python ./app.py
