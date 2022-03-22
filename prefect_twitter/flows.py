"""This is an example flows module"""
from prefect import flow

from prefect_twitter.tasks import (
    goodbye_prefect_twitter,
    hello_prefect_twitter,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_twitter)
    print(goodbye_prefect_twitter)
