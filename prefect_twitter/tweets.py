"""This is a module for interacting with Twitter tweets"""
from functools import partial
from prefect import task
from anyio import to_thread
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from prefect_twitter import TweepyCredentials

@task
async def create_tweet(text: str, tweepy_credentials: "TweepyCredentials", **kwargs):
    client = tweepy_credentials.get_client()
    partial_create = partial(client.create_tweet, text=text, user_auth=False, **kwargs)
    response = await to_thread.run_sync(partial_create)
    return response
