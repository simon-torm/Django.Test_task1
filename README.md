# Django.Test_task1
REST API for a portfolio publication site

## Models:
* User
* Portfolio
* Image
* Comment

## Project launch
1) portfoliosite/portfoliosite/settings.py - change database settings.
2) Migrate. Enter **"python manage.py migrate"**
3) Enter **"python manage.py createsuperuser"** in the terminal and create a new admin profile..
4) Run server **"python manage.py runserver"**

**http://localhost:port/docs/** - here you will find API documentation

## API
* Portfolios (GET, POST, PUT, DELETE) - **http://host:port/api/portfolios/**
* Images (GET, POST, PUT, DELETE) - **http://host:port/api/images/**
* Comments (GET, POST) - **http://host:port/api/comments/**
* Search (GET) - **http://host:port/api/search/**
