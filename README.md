# prefect-twitter

## Welcome!

Prefect integrations for interacting with Twitter.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-twitter` with `pip`:

```bash
pip install prefect-twitter
```

### Write and run a flow

Tweets an update with just text.
```python
from prefect import flow
from prefect_twitter import TwitterCredentials
from prefect_twitter.tweets import update_status

@flow
def example_update_status_flow():
    twitter_credentials = TwitterCredentials(
        consumer_key="consumer_key",
        consumer_secret="consumer_secret",
        access_token="access_token",
        access_token_secret="access_token_secret"
    )
    status_id = update_status(twitter_credentials, status="A Prefect Tweet!")
    return status_id

example_update_status_flow()
```

## Resources

If you encounter and bugs while using `prefect-twitter`, feel free to open an issue in the [prefect-twitter](https://github.com/PrefectHQ/prefect-twitter) repository.

If you have any questions or issues while using `prefect-twitter`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-twitter` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-twitter.git

cd prefect-twitter/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
