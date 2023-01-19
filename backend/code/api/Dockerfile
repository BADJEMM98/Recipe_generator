# Sets the base image for subsequent instructions
FROM ubuntu:20.04
# Sets the working directory in the container  
WORKDIR /app
RUN mkdir -p /app/logs
RUN mkdir -p /var/log/supervisor
RUN apt -y update && apt install -y python3-pip
RUN apt-get update && apt-get install -y --force-yes supervisor
# Copies the dependency files to the working directory
COPY requirements.txt /app

#COPY supervisor.conf /etc/supervisor/conf.d/supervisord.conf
# Install dependencies
RUN pip install -r requirements.txt

# Copies everything to the working directory
COPY . /app
VOLUME /app

# Command to run on container start    
CMD ./deployment/run.sh
