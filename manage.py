import pytest
from sanic_script import Manager

from api import create_app
from api.services.logging import log
from api.settings.detect_aws import check_and_return_ec2_env


# run the aws detect ahead of time.
SETTINGS = check_and_return_ec2_env()
log.info(f"SETTINGS: {SETTINGS}")

# create the application.
app = create_app("sanic-python-api", SETTINGS.get("ENVIRONMENT", "DEV"))

# Factory manager, allows multiple instances of bases with differing settings.
manager = Manager(app)


@manager.command
def run():
    app.run(debug=False, port=8000)


@manager.command
def test():
    result = pytest.main()
    print(f"Pytest Results: {result}")


if __name__ == '__main__':
    manager.run()
