# Car REST API

REST API created for practice purpose. Basic CRUD implemented using Django REST Framework. Application is divided into 2 containers: DRF (web) and Postgres (db).

## Table of contents

- [Technologies](#technologies)
- [Setup](#setup)
- [Commands](#commands)
- [Tests](#tests)
- [Contact](#contact)

## Technologies

- Python version: 3.7
- Django version: 3.1.1
- DRF version: 3.11.1
- Docker version: 19.03.6

## Setup

To create virtual environment:

```
python3 -m venv venv
```

To build container:

```
docker-compose build
```

To migrate database:

```
docker-compose run web python manage.py migrate
```

To create superuser:

```
docker-compose run web python manage.py createsuperuser
```

To load already-prepared data:

```
docker-compose run web python manage.py loaddata users.json
docker-compose run web python manage.py loaddata cars.json
```

## Commands

To run containers:

```
docker-compose up
```

To list all objects or add new object:

```
http://127.0.0.1:8000/cars/
```

To detail specified object by id:

```
http://127.0.0.1:8000/cars/<id>
```

To delete specified object by brand or model:

```
http://127.0.0.1:8000/cars/?q=<brand_or_model>
```

To change format of display (api or json):

```
http://127.0.0.1:8000/cars/?format=<format>
```

To get an access token (JWT) using username and password:

```
http://127.0.0.1:8000/auth/obtain-jwt-token/
```

To refresh a token:

```
http://127.0.0.1:8000/auth/refresh-token/
```

To verify a token:

```
http://127.0.0.1:8000/auth/verify-token/
```

## Tests

To run tests:

```
docker-compose run web python manage.py test
```

## Create Fixture Data

After adding data using django admin panel, to enter the docker container in bash:

```
docker-compose run web bash
```

Then to create the fixtures:

```
python manage.py dumpdata --exclude auth.permission --exclude sessions --exclude contenttypes --exclude admin.logentry --exclude cars.car > users.json
python manage.py dumpdata --exclude auth.permission --exclude sessions --exclude contenttypes --exclude admin.logentry --exclude auth.user > cars.json
```

A good reference can be found here: [Django dumpdata and loaddata](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)

## Contact

Created by Adam Misiak
