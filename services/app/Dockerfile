# pull the official docker image
FROM python:3.10-slim

# set work directory
WORKDIR /app

# set env variables
ENV FLASK_APP=manage.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# update pip
RUN pip install --upgrade pip


# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 5000

# run server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]