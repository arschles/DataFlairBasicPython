#Pull Python Image
FROM ubuntu:20.04

#run commands to download python
RUN apt-get update -y && \
        apt-get install -y python3-pip python3-dev git 

#Copy the requirement.txt file..?
COPY ./requirements.txt /app/requirements.txt

#Declare Working Directory
WORKDIR /app

#Run install command for all the dependencies
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["main.py"]



