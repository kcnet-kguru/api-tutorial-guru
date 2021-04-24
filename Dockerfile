FROM python:3.9-slim-buster

WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "app.wsgi:application"]