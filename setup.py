from setuptools import setup, find_packages

setup(
    name="my_memo_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-login",
        "flask-wtf",
    ],
) 