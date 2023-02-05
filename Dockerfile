FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget python3 python3-dev python3-pip

# Set the working directory
WORKDIR /app

# Copy the model code to the container
COPY . ./

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

EXPOSE 9092 2181