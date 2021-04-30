FROM python:3.9-slim

RUN pip install flask gunicorn

WORKDIR /usr/app
COPY ./app .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
