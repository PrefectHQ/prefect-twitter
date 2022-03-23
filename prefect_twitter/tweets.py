"""This is a module for interacting with Twitter tweets"""

from functools import partial
from typing import TYPE_CHECKING, List, Optional, Union

from anyio import to_thread
from prefect import get_run_logger, task

if TYPE_CHECKING:
    from prefect_twitter import TwitterCredentials


@task
async def update_status(
    twitter_credentials: "TwitterCredentials",
    status: Optional[str] = None,
    media_ids: Optional[List[Union[int, str]]] = None,
    **kwargs: dict
) -> int:
    """
    Updates the authenticating user's current status, also known as Tweeting.

    Args:
        twitter_credentials: Credentials to use for authentication with Tweepy.
        status: Text of the Tweet being created. This field is required
            if media_ids is not present.
        media_ids: A list of Media IDs being attached to the Tweet.
        kwargs: Additional keyword arguments to pass to update_status.
    Returns:
        The status ID.

    Example:
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

        Tweets an update with text and a media.
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
            media_id = media_upload("prefect.png", twitter_credentials)
            status_id = update_status(
                twitter_credentials,
                status="Prefect!",
                media_ids=[media_id]
            )
            return status_id

        example_update_status_flow()
        ```
    """
    num_media = len(media_ids) if media_ids else 0
    logger = get_run_logger()
    logger.info("Updating status with %s media.", num_media)

    if status is None and media_ids is None:
        raise ValueError("One of text or media_ids must be provided")

    api = twitter_credentials.get_api()
    partial_update = partial(
        api.update_status, status=status, media_ids=media_ids, **kwargs
    )
    status = await to_thread.run_sync(partial_update)
    return status.id
