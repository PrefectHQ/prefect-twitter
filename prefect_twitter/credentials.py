"""Credential classes used to perform authenticated interactions with Twitter"""

from prefect.blocks.core import Block
from pydantic import SecretStr
from tweepy import API, OAuth1UserHandler


class TwitterCredentials(Block):
    """
    Block used to manage Twitter authentication with tweepy.
    See Authentication Tokens section of the Keys and Tokens tab of
    your app, under the Twitter Developer Portal Projects & Apps page at
    https://developer.twitter.com/en/portal/projects-and-apps.

    Args:
        consumer_key: This is also known as oauth_consumer_key or API key.
        consumer_secret: This is also known as oauth_consumer_secret or API secret key.
        access_token: This is also known as oauth_token.
        access_token_secret: This is also known as oauth_token_secret.

    Example:
        Load stored Twitter credentials:
        ```python
        from prefect_twitter import TwitterCredentials
        twitter_credentials_block = TwitterCredentials.load("BLOCK_NAME")
        ```
    """  # noqa E501

    _block_type_name = "Twitter Credentials"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/1NyN5egjNk9Sel17rs0cTz/067bb478b4fec22d8aa47b79b085a6e9/twitter.png?h=250"  # noqa

    consumer_key: str
    consumer_secret: SecretStr
    access_token: str
    access_token_secret: SecretStr

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
            self.consumer_secret.get_secret_value(),
            self.access_token,
            self.access_token_secret.get_secret_value(),
        )
        api = API(auth=auth)
        return api
