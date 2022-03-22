"""Credential classes used to perform authenticated interactions with Twitter"""

from dataclasses import dataclass
from tkinter import E
from typing import Optional, Union

from tweepy import Client

@dataclass
class TweepyCredentials:
    """
    Dataclass used to manage Twitter authentication with tweepy.
    See Authentication Tokens section of the
    Keys and Tokens tab of your app, under the
    Twitter Developer Portal Projects & Apps page at
    https://developer.twitter.com/en/portal/projects-and-apps

    Args:
        bearer_token: Token to authenticate for developer app.
    """

    bearer_token: Optional[str]

    def get_client(self) -> Client:
        """
        Gets an authenticated Tweepy client.

        Returns:
            Client: An authenticated Tweepy client.

        Example:
            Gets a Tweepy client.
            ```python
            from prefect import flow
            from prefect_twitter import TweepyCredentials

            @flow
            def example_get_client_flow():
                tweepy_credentials = TweepyCredentials(
                    bearer_token="bearer_token"
                )
                client = tweepy_credentials.get_client()
                return client

            example_get_client_flow()
            ```
        """
        client = Client(bearer_token=self.bearer_token)
        return client
