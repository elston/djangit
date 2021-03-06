Django Webpack Starter Kit
=========================

Yet another boilerplate for building web application 


Technology
----------

* Docker
* Python 3.5
* Django
* Nodejs
* Flow
* Webpack 4
* Postgres 9.6
* Nginx
* Gunicorn
* Virtualenv


Common features
----------------

* Docker (and docker-compose) containerized
* Automated control start and down through 'make'

Backend features
----------------

* Django  - ah.. popular framework
* Automated scripts for bootstrap and db migrate
* ipdb for trace when debugging in dev mode
* Gunicorn starting script for production
* Gunicorn starting script with logging for testing
* Specialized template tag - Django-Webpack (slightly modified :) great thanks [Owais Lone](https://github.com/owais) for idea ) that enable to avoid preloaded cache with js and other resource in browsers due to use hash in resource name. Use with popularyty webpack plugin [webpack-assets-manifest](https://github.com/webdeveric/webpack-assets-manifest), thanks Eric aka webdeveric.
* PostgreSQL container on debian with bootstrapping script allowed to substitution db name, user and password from environment variable into db creation script


Frontend features
-----------------

* Nodejs with babel-node for use latest ECMAScript specifications to available still at the prepare stage for running webpack and(or) browsersync, that extremely conveniently
* The possibility to run building scripts with debugging mode (see scripts in package.json - build:inspect). To make trace is need put command ``` debugging ``` in code and open google chrome browser tab in ```chrome://inspect``` (you can see the catched socket yours node js, in this project it on port 9229)
* There is Browsersync configuration for developing with proxy that pass on backend(in this project, in inner docker network, it is ``` http://backer ``` ) all requests excluding static resources (js,css,images,fonts)
* Most famous styles loaders (scss, less, stylus)
* Webpack 4 config with most famous features:
    - multiple entry point
    - splitting output script for vendor chank and default chank
    - output resource name with hash
    - building manifest with [webpack-assets-manifest](https://github.com/webdeveric/webpack-assets-manifest)
    - extracting styles to a separate file for separate loading
* React 16
* Flow - static type checker for javascript [link](https://flow.org/)
![flow in work](https://github.com/elston/djangit/blob/master/screenshots/flow.png  "flow in work")

* Style from bootstrap, font-awesome on scss 



Getting Started for Local Development
=====================================


Installing and bootstraping
---------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's

In the project books ./book/dev/ (where the `Makefile` file is located), run:

```
make build
```

then

```
make bootstrap
```

then

```
make db
```

then test db

```
psql -U [user name] -h localhost
```

if all OK, down db

```
make down
```

then migrate db

```
make migrate_backer
```


Helper commands
---------------

### To run any command inside the Docker container
```
make shell_[name of container]
```


### To view Docker images in current project

```
make images
```

### To view runing Docker containers in current project

```
make ps
```

Running Local Development servers
=================================


### 1. Running backend (backer) server

Open terminal in flaskit/book/dev (where the `Makefile` file is located) and run command

```
make shell_backer
```


### 2. Running frontend container

Open another terminal tab  in flaskit/book/dev (where the `Makefile` file is located) and run command

```
make shell_fronter
```

### 3. Running frontend (fronter) server

after docker container is running, run fronter server, wich make manifest.json wich need to get path resources (js, css , images, fonts ...etc.) in templates on backend server

```
cd /fronter
yarn [name of commands from packege.json]
```

### 4. Running backend (backer) server

```
runserver.sh
```

### 5. Running browser

open in browser tab to url ```http://localhost:3000```



Running testing and production servers(* not complete)
=================================================================


### This will start the containers in the background.

```
make up
```

When you need finish all containers:

```
make down
```

### View the logs

```
docker logs [-f] [name of container getting from docker ps -a]
```

In production servers (* not complete)
=================================================================

For compile frontend statics go in folder ``` books/prod ``` run command

```
make compile_fronter
```


Acknowledgment
==============

* kriasoft - [react-starter-kit](https://github.com/kriasoft/react-starter-kit)
* Cory House - [react-slingshot](https://github.com/coryhouse/react-slingshot)
* Steven Loria - [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)
* Owais Lone - [django-webpack-loader](https://github.com/owais/django-webpack-loader)
