from tweepy import API

from prefect import flow
from prefect_twitter import TweepyCredentials


def test_tweepy_credentials_get_api():
    consumer_key = "consumer_key"
    consumer_secret = "consumer_secret"
    access_token = "access_token"
    access_token_secret = "access_token_secret"
    tweepy_credentials = TweepyCredentials(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    api = tweepy_credentials.get_api()
    assert isinstance(api, API)
