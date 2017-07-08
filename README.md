# flask-api-boilerplate
A Flask boilerplate for building a Dockerized API

## Prerequisites

Need to have [Docker](https://docs.docker.com/engine/installation/) installed.

## Getting Started
1. Clone or download the repo.
2. Open `Dockerfile` and change `MAINTAINER` to your name and email.
3. Open `docker-compose.yml` and change `flaskboilerplate` to the name of your app.
4. Rename `.env-example` to `.env` (make sure git does not track this file).
5. Open `.env` and change `COMPOSE_PROJECT_NAME` to the name of your app, and choose a username and password for your PostgreSQL database.
6. Open `setup.py` and change the `name` variable and the word "boilerplate" inside `entry_points` to the name of your app.
7. Open `config/settings.py` and change `SQLALCHEMY_DATABASE_URI` to `postgresql://usernamefrom#5:passwordfrom#5@postgres:5432/usernamefrom#5`. Also change the mail settings to your gmail credentials if you plan on using email in the app.
8. Run `docker-compose up --build`
9. Before you can use the app, you need to initialize the tables in the database. The boilerplate comes with a single table, `users`. In order to initialize it, run `docker ps` and get the container id of the running app. Then run `docker exec CONTAINER_ID appname db init`. If everything works you'll see a message saying the tables were droppped and reinitialized. **WARNING:** Do not run this command in production. This is only to be used during development. In production, if you change your db schemas, run migrations. If the above command gives an error, you'll need to run `pip install --editable .` and you should only need to run this command once. 

## Security
Storing passwords and other sensitive information in version control is a bad idea. The following are some suggestions of how to secure your source code. 
1. Create an `instance` directory and add `__init__.py` and `settings.py` files inside. All publicly facing settings of your app should go into `config/settings.py` but everything you put in `instance/settings.py` will override those in the `config` directory. For example, instead of putting the db url as instructed in step 6 above in `config/settings.py`, you should put it in `instance/settings.py` and keep a dummy url in `config/settings.py`. 

## Running Tests
To run the unit tests: `docker exec CONTAINER_ID appname tests`
To run them with a coverage report: `docker exec CONTAINER_ID appname tests cov`. This will place the coverage reports inside a `tmp` directory. 

## Blueprints
You can create and delete blueprints with cli commands. Creating a blueprint will create the module with the given name inside the `blueprints` directory with `routes.py` and `models.py` files inside. The `routes.py` will have minimal code setup. Deleting a blueprint will delete all of its contents.

- To Create: `docker exec [CONTAINER_ID] [APPNAME] blueprint create [BLUEPRINTNAME]`
- To Delete: `docker exec [CONTAINER_ID] [APPNAME] blueprint delete [BLUEPRINTNAME]`

## Acknowledgements
This boilerplate is heavily influenced by what I learned from these two sources:
- [Nick Janetakis's Udemy Course](https://www.udemy.com/the-build-a-saas-app-with-flask-course/learn/v4/overview)
- [Miguel Grinberg's Book](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1449372627/ref=sr_1_2?ie=UTF8&qid=1491529179&sr=8-2&keywords=flask+book)
