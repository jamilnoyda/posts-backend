# posts-backend

First, clone the repository to your local machine:

git clone https://github.com/jamilnoyda/onlineshop.git

Install the requirements:

pip install -r requirements.txt --user

python manage.py migrate
python manage.py runserver
admin login
add fixtures:
python manage.py loaddata fixtures/data.json
jamilnoyda@gmail.com
pass: hellohello


Finally, run the development server:

python manage.py runserver

The project will be available at 127.0.0.1:8000.


 python verstion  python 3.8
  django 3.x


python manage.py dumpdata --format=json > fixtures/data.json 




add exmaple of curl in this file


curl -H "Authorization: Bearer 6suQgkwNdHmYP5YsdBA5IB32MO7KFW" http://localhost:8000/groups/


heroku logs --tail -a  posts-backend-python


 gunicorn posts_backend.wsgi --log-file -




# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)





## only for  deployment


Install the Heroku CLI

Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login

Clone the repository

Use Git to clone posts-backend-python's source code to your local machine.

$ heroku git:clone -a posts-backend-python
$ cd posts-backend-python

Deploy your changes

Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master



# only for deployment ===dockerhub===

Install the Heroku CLI

Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login

Log in to Container Registry

You must have Docker set up locally to continue. You should see output when you run this command.

$ docker ps

Now you can sign into Container Registry.

$ heroku container:login

Push your Docker-based app

Build the Dockerfile in the current directory and push the Docker image.

$ heroku container:push web

Deploy the changes

Release the newly pushed images to deploy your app.

$ heroku container:release web

