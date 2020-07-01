# sanic-python-api #

This aim of this project is to build a baseline for future api based projects on a asynchronous framework. This baseline, 
will aim to make use of the follwoing technologies:
1. AWS and some of its inherent use cases. 
2. Relational DB.  
3. Redis Caching and no-sql.

### What is this repository for? ###
The repo is to act as a baseline for asynchronous micro services in python.

# Version
To be determined

### How do I get set up? ###

# Docker support:


# Setup procedure is included in the entrypoint.sh script. The script does the following:

* Summary of set up

* Configuration

* Dependencies

* Database configuration
    # SQL DB:
    Always connect to the local sqlite main.db file.

    # Redis:
    Local redis instance.

* How to run tests
    1. pytest
    2. curl localhost:8000/v1/health


* Deployment instructions

# From entrypoint.sh
init:
  mkdir database
  mkdir api/logs
  touch api/logs/api.log
  touch api/logs/api_stderr.log

	python3.7 -m venv venv; \
	echo 'source venv/bin/activate' >> .env; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \
	pip3 install -e .

update_deps:
	source ./venv/bin/activate; \
	pip install --upgrade -r requirements.txt; \

revision:
	alembic revision --autogenerate;

upgrade:
	alembic upgrade head

### Contribution guidelines ###

* Writing tests
    All pytests should be contributed to the test folder in path: sanic-python-api/test
* Code review
    Pull requests to be submitted and approved per team situation.
* Other guidelines
    N/A

### Who do I talk to? ###
Kevin: @ kevinsmith.kis@gmail.com


# When addressing available insurers,

# How to use Alembic in this Project
# make tags and referral a toggle able function.

# Deployment procedure:

1. create the venv.
2. Run the venv.
3. install the requirements
4. install pip install -e .
5. alembic, double step
5.1 alembic revision --autogenerate;
5.2 alembic upgrade head
6. supervisor.


command=/venv/bin/gunicorn manage:app --bind 0.0.0.0:8000 -t 1200 --worker-class sanic.worker.GunicornWorker -w 4