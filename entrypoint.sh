init:
  mkdir database
  mkdir api/logs
  touch api/logs/api.log
  touch api/logs/api_stderr.log

	python3.6 -m venv venv; \
	echo 'source venv/bin/activate' >> .env; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \
	pip3 install -e .

revision:
	alembic revision --autogenerate;

upgrade:
	alembic upgrade head
