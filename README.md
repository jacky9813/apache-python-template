# Template Project for Apache HTTP Server with Python 3 CGI Support

## Directories
* apache-python-image: Where the Dockerfile for main image is defined
* cgi-bin: Where Python script is located
* htdocs: Static web page

## Build
To run this image, simply issue the command
```bash
# docker-compose up
```

## Python Module
To add module(s) to Python 3 either using PIP or APT, rewrite Dockerfile in apache-python-image like:
```Dockerfile
FROM httpd:2.4
RUN apt-get update && apt-get install -y python3 apt-utils coreutils python3-pip python3-SOMEMODULE && apt-get upgrade -y
RUN pip3 install SOMEMODULE
```
And then rebuild it with command
```bash
# docker-compose up --build
```
