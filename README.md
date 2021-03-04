# CustomerOrders_Service
#### By Lourine Millicent
## Description
 A Python RESTful API that enables one to input/upload customer and order data in a Postgres Database. It uses  Africa's Talking SMS  Gateway to send customers sms alerts when their order is added, unittesting with coverage, and CI/CD through Travis CI. It also implements JWT for authentication

## User Stories
* As a user, I would like to register
* As a user, I would like to sign in to the API
* As a user, I would like to add an order
* As a user, I would like to view my orders
* As a user, I would like to update or delete orders I have created.
* As a user, I would like to get an sms alert when an order is added


## Technologies Used
  * Python 3.8
  * Django Rest Framework
  * Postgressql
  * Heroku
  * Africa's Talking Sandbox API

## BDD

>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Customer username(email), ``eg wangari@example.com``|
| Password  | Customer password, ``eg pass1234``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | customer username, ``eg wangari``|
| Email  | custiomer email, ``eg wangari@gmail.com``|
|Phone_number|customer phone_number
| Password  | customer password, ``eg pass1234``|


> Order Post inputs

| Inputs | Description  |
|---|---|
|  Item | ``Plywood``|
| Amount| 20000|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Lourine/CustomerOrder_Service
        $ cd CustomerOrder_Service

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
* Run pip3 install -r requirements.txt on your virtual environment
* Open psql shell and create Postgres database
* touch .env on your root directory and include all configs in .env.sample in your .env file
* Set MODE='dev' for your development environment.
* python manage.py migrate
* Register for Sandbox credentials on [Africa's Talking](https://africastalking.com/)

* To run the application, in your terminal:

        $ python3.8 manage.py runserver

* Open the application on your browser `127.0.0.1:8000`.

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests



### To contribute to this project on any modules, follow these easy steps:

- Fork the repo
- Create a new branch in your terminal (git checkout -b improve-feature)
- Make appropriate changes in file(s)
- Add the changes and commit them (git commit -am "Improve App")
- Push to the branch (git push origin improve-app)
- Create a Pull request

## Contact Information 

If you have any question or contributions, please email me at [lourine.millicent@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Lourine Millicent*