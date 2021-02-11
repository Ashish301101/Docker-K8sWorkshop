# Orchestration!
So, you will notice we have structured our code a little.
- `/app` folder has all the Flask app image related scripts
- `/db` folder has the init script for our db

We focus on Orchestration in this phase.
We will deploy two containers --> flask `app` and mysql `db`
1. we will manually deploy and connect the services
2. we will use docker-compose to deploy the two services.


First up, we upgarde our basic flask app to be connected with a database (mysql) in our case.

Add interface to get names of all the subjects. Head to docker-manual/app/app.py to see what changed.
In the `docker-manual/db/init.sql` you can modifythe subjects and subject codes and even your db schema.

## Manually Deploying
In `/docker-manual` directory.
1. Build the app -> ```sudo docker build --tag flask-app-2 ./app/```
2. Build the db -> ```sudo docker build --tag mysql-db ./db/```
3. Run the db first -> ```sudo docker run -d --name db -p 32000:3306 -v db:/docker-entrypoint-initdb.d/:ro mysql-db```
   I would suggest we verify if the db is actually running.
   If you do have mysql client available locally
   ``` mysql -h localhost -P 32000 --protocol=tcp -u root  -p```
   This would prompt you for a password -> `root`
   This should let you into the mysql shell
   `mysql> show databases;`
   And verify that you see `subjects` there.

   If you have the mysql-connector python library
   you can modify the host, port in app.py and run the app.py locally to test.
4. Now let us dive into some basic networking of docker containers.
   If you execute ```docker network ls``` you will notice a bridge and a host network.
   When we run a container without explicitly specifying any network, it is associated to the bridge network.
   In such cases though these containers are on the same network they can access each other only via IP addresses.
   To make them access each other my names, we need to use links which are deprecated.
   Let us inespect the bridge network.
   `docker inspect bridge`
   You should be able to see the containers associated and the IP addresses.
   Find the IP address of the container with the name `db`
   And copy it to the app/app.py line number 16.

   We proceed to running the app.
   ```sudo docker run --name flask-app-2 -p 5001:5000 flask-app-2```

   Redirect to the following IP on your browser/postman.
   ```http://0.0.0.0:5001/subjects```

   You should be able to see a json dump of the subjects that are added using the init.sql script.

I suggest you stop and remove both the containers we started.

`docker rm -f flask-app-2; docker rm -f db`

## Docker-compose
So, manually deploying and connecting containers is a task and cannot be done practically in the production environment.
It is tedious for development as well for that matter.
Don't worry we have a quick solution to simplify orchestration! We can use a `docker-compose.yml` file to configure all of this and run it together!

Lets go through our compose file
- **build**: specifies the directory which contains the Dockerfile containing the instructions for building this service
- **links**: links this service to another container. This will also allow us to use the name of the service instead of having to find the ip of the database container, and express a dependency which will determine the order of start up of the container
- **ports**: mapping of `<Host>:<Container>` ports.
- **image**: Like the FROM instruction from the Dockerfile. Instead of writing a new Dockerfile, we are using an existing image from a repository. It’s important to specify the version — if your installed mysql client is not of the same version problems may occur.
- **environment**: add environment variables. The specified variable is required for this image, and as its name suggests, configures the password for the root user of MySQL in this container. More variables are specified here.
- **ports**: Since I already have a running mysql instance on my host using this port, I am mapping it to a different one. Notice that the mapping is only from host to container, so our app service container will still use port 3306 to connect to the database.
- **volumes**: since we want the container to be initialized with our schema, we wire the directory containing our `init.sql` script to the entry point for this container, which by the image’s specification runs all .sql scripts in the given directory.

```docker-compose build```
```docker-compose up```

Thats it, your services are up and running!

Redirect to the following IP on your browser/postman :
```http://0.0.0.0:5001/subjects```

You should be able to see a json dump of the subjects that are added using the `init.sql` script.
