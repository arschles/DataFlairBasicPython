#FROM ubuntu:20.04

#RUN apt-get update -y && \
        #apt-get install -y python3-pip python-dev git

#COPY ./requirements.txt /app/requirements.txt

#WORKDIR /app

#RUN pip3 install -r requirements.txt

#COPY . /app

#CMD ["python3","-m","flask","run"]

FROM python:3.8

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY . /app

CMD ["python","-m","flask","run"]
