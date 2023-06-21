FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# Expose the port on which the Django app will run
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
