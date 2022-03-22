"""Credential classes used to perform authenticated interactions with Twitter"""

from dataclasses import dataclass
from typing import Optional, Union

from tweepy import API, OAuth2BearerHandler, OAuth2AppHandler, OAuth1UserHandler

@dataclass
class TweepyCredentials:
    """
    Dataclass used to manage Twitter authentication with tweepy.
    Provide either bearer token, or all of consumer_key, consumer_secret,
    access_token, access_token_secret. See Authentication Tokens section of the
    Keys and Tokens tab of your app, under the
    Twitter Developer Portal Projects & Apps page at
    https://developer.twitter.com/en/portal/projects-and-apps.

    Args:
        bearer_token: Token to authenticate for developer app.
        consumer_key: also known as oauth_consumer_key or API key
        consumer_secret: also known as oauth_consumer_secret or API secret key
        access_token: also known as oauth_token
        access_token_secret: also known as oauth_token_secret
    """

    bearer_token: Optional[str] = None
    consumer_key: Optional[str] = None
    consumer_secret: Optional[str] = None
    access_token: Optional[str] = None
    access_token_secret: Optional[str] = None

    def get_api(self) -> API:
        """
        Gets an authenticated Tweepy API.

        Returns:
            An authenticated Tweepy API.

        Example:
            Gets a Tweepy API using a bearer token.
            ```python
            from prefect import flow
            from prefect_twitter import TweepyCredentials

            @flow
            def example_get_api_flow():
                bearer_token = "bearer_token"
                tweepy_credentials = TweepyCredentials(
                    bearer_token=bearer_token
                )
                api = tweepy_credentials.get_api()
                return api

            example_get_api_flow()
            ```

            Gets a Tweepy APi using consumer and access pairs.
            ```python
            from prefect import flow
            from prefect_twitter import TweepyCredentials

            @flow
            def example_get_api_flow():
                consumer_key = "consumer_key"
                consumer_secret = "consumer_secret"
                access_token = "access_token"
                access_token_secret = "access_token_secret"
                tweepy_credentials = TweepyCredentials(
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret
                )
                api = tweepy_credentials.get_api()
                return api

            example_get_api_flow()
            ```
        """
        consumer_pair = (
            self.consumer_key,
            self.consumer_secret
        )
        access_pair = (
            self.access_token,
            self.access_token_secret
        )
        credentials = consumer_pair + access_pair
        if self.bearer_token:
            auth = OAuth2BearerHandler(self.bearer_token)
        elif all(val for val in credentials):
            auth = OAuth1UserHandler(*credentials)
        elif all(val for val in consumer_pair):
            auth = OAuth2AppHandler(*consumer_pair)
        else:
            raise ValueError(
                "Either a bearer token, a pair of consumer credentials, or "
                "both pairs consumer and access credentials must be provided"
            )
        api = API(auth=auth)
        return api
