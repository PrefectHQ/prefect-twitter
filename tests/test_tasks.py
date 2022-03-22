from prefect import flow

from prefect_twitter.tasks import (
    goodbye_prefect_twitter,
    hello_prefect_twitter,
)


def test_hello_prefect_twitter():
    @flow
    def test_flow():
        return hello_prefect_twitter()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-twitter!"


def goodbye_hello_prefect_twitter():
    @flow
    def test_flow():
        return goodbye_prefect_twitter()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-twitter!"
