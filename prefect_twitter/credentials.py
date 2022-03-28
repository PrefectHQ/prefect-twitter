"""Credential classes used to perform authenticated interactions with Twitter"""

from dataclasses import dataclass

from tweepy import API, OAuth1UserHandler


@dataclass
class TwitterCredentials:
    """
    Dataclass used to manage Twitter authentication with tweepy.
    See Authentication Tokens section of the Keys and Tokens tab of
    your app, under the Twitter Developer Portal Projects & Apps page at
    https://developer.twitter.com/en/portal/projects-and-apps.

    Args:
        consumer_key: also known as oauth_consumer_key or API key
        consumer_secret: also known as oauth_consumer_secret or API secret key
        access_token: also known as oauth_token
        access_token_secret: also known as oauth_token_secret
    """

    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str

    def get_api(self) -> API:
        """
        Gets an authenticated Tweepy API.

        Returns:
            An authenticated Tweepy API.

        Example:
            Gets a Tweepy API using consumer and access pairs.
            ```python
            from prefect import flow
            from prefect_twitter import TwitterCredentials

            @flow
            def example_get_api_flow():
                consumer_key = "consumer_key"
                consumer_secret = "consumer_secret"
                access_token = "access_token"
                access_token_secret = "access_token_secret"
                twitter_credentials = TwitterCredentials(
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret
                )
                api = twitter_credentials.get_api()
                return api

            example_get_api_flow()
            ```
        """
        auth = OAuth1UserHandler(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret,
        )
        api = API(auth=auth)
        return api
