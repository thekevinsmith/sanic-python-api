import os
from setuptools import find_packages, setup

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"Dir:{dir_path}")

# try:  # for pip >= 10
#     from pip._internal.req import parse_requirements

# CODE_DIR = ""
# if os.environ.get("BITBUCKET_CLONE_DIR"):
#     CODE_DIR = os.environ.get("BITBUCKET_CLONE_DIR", "") + "/ctrl_api/"
# elif os.environ.get("CODE_DIR"):
#     CODE_DIR = os.environ.get("CODE_DIR", "") + "/"
# else:
#     CODE_DIR = f"{dir_path}/sanic-python-api/"
#
# install_require = parse_requirements(
#     filename=f"{CODE_DIR}requirements.txt", session="hack"
# )

# install_reqs = list([str(ir.req) for ir in install_require if ir.req])

setup(
    name="sanic-python-api",
    # python_requires=">=3.7.3",
    version="1.1.1",
    include_package_data=True,
    # install_requires=install_reqs,     # TODO: fix
    setup_requires=["pytest-runner"],
    # tests_require=install_reqs,        # TODO: fix
    package_data={"": ["*.json"]},
    extras_require={"dev": ["black==19.3b0", "profilehooks", "xar"]},
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
)