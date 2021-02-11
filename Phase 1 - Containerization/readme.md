# Containerization!

In this Phase you learn how you can dockerise an application.

1. Run ```python3 app.py```
   This just runs the python script and starts the flask app
   Head to your browser/ postman and redirect to ```http://localhost:5000```
   Currently this python application is running in the foreground and can be stopped  with a simple Ctrl+C
2. We will now dockerize this application.
   Dockerize meaning -> we will run the same application inside a docker container.

## What the dockerfile does
`FROM python:alpine3.7` pulls python 3.7’s image from the docker hub
`COPY` command copies the flask app into the container
`WORKDIR` command sets the working directory.
`RUN pip install -r requirements.txt` this command will install each requirement written in `requirements.txt` file one by one bye on the host system.
`EXPOSE` as the name says exposes port 5000 which Flask app will use to the container so that later it can be mapped with the system’s port.
Entrypoint and CMD together just execute the command `python app.py` which runs this file.

Before we proceed let's ensure each one of you have Docker installed
```docker -v```
## Building the image
```sudo docker build --tag flask-app .```
Running this command will build a container image named flask-app
```docker image ls | grep flask-app```
Run the above command, you should be able to see flask-app in the list.
## Running the image
```docker run --name flask-app -p 5001:5000 flask-app ```
   -name parameter gives name to the container (This is not mandatory, you get a system generated name otherwise)
   -p parameter maps the host/(your laptop) port 6000 to the container’s port 5000 since the container is isolated
      and we need to map it in order to access it from external. environment.
      Recall you exposed the port 5000 of your container so that you could map it.
Lastly flask-app specifies the name of the image.
Running this command will expose the app to port no 5001 on local.
Head to ```http://localhost:5001``` and check it out.
This will run your container in interactive mode. To run in background/ detach use the -d option.

This will generally work until there is a port conflict on your local system. In this case, try a different port instead of 5001.
A better way of keeping a check on the used/free ports s using ```netstat -anp | find ":<port number>"```

To check is the container is running use  ```docker ps```

So, now you know how you can run an app/script inside docker.

A task for later -> try pushing the docker image to the docker registry.

