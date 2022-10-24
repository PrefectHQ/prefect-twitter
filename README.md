# prefect-twitter

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-twitter/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-twitter?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-twitter/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-twitter?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-twitter/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-twitter?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-twitter/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-twitter?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

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

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_twitter
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

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

Feel free to ⭐️ or watch [`prefect-twitter`](https://github.com/PrefectHQ/prefect-twitter) for updates too!

## Development

If you'd like to install a version of `prefect-twitter` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-twitter.git

cd prefect-twitter/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```