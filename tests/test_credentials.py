from tweepy import API

from prefect_twitter import TwitterCredentials


def test_twitter_credentials_get_api():
    consumer_key = "consumer_key"
    consumer_secret = "consumer_secret"
    access_token = "access_token"
    access_token_secret = "access_token_secret"
    twitter_credentials = TwitterCredentials(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    api = twitter_credentials.get_api()
    assert isinstance(api, API)
