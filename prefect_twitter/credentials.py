"""Credential classes used to perform authenticated interactions with Twitter"""

from prefect.blocks.core import Block
from pydantic import VERSION as PYDANTIC_VERSION

if PYDANTIC_VERSION.startswith("2."):
    from pydantic.v1 import Field, SecretStr
else:
    from pydantic import Field, SecretStr

from tweepy import API, OAuth1UserHandler


class TwitterCredentials(Block):
    """
    Block used to manage Twitter authentication with tweepy.
    See Authentication Tokens section of the Keys and Tokens tab of
    your app, under the Twitter Developer Portal Projects & Apps page at
    https://developer.twitter.com/en/portal/projects-and-apps.

    Attributes:
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
    _logo_url = "https://cdn.sanity.io/images/3ugk85nk/production/747aa724fedcefd1c1cec248ab7a5b518a1191cd-250x250.png"  # noqa
    _documentation_url = "https://prefecthq.github.io/prefect-twitter/credentials/#prefect_twitter.credentials.TwitterCredentials"  # noqa

    consumer_key: str = Field(
        ..., description="Twitter App API key used for authentication."
    )
    consumer_secret: SecretStr = Field(
        ..., description="Twitter App API secret used for authentication."
    )
    access_token: str = Field(
        ..., description="Oauth token used to access the Twitter API."
    )
    access_token_secret: SecretStr = Field(
        ..., description="Ouath secret used to access the Twitter API."
    )

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
