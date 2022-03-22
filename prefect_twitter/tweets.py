"""This is a module for interacting with Twitter tweets"""

from functools import partial
from typing import TYPE_CHECKING, List, Optional, Union

from anyio import to_thread
from prefect import get_run_logger, task

if TYPE_CHECKING:
    from tweepy.models import Status

    from prefect_twitter import TweepyCredentials


@task
async def update_status(
    tweepy_credentials: "TweepyCredentials",
    status: Optional[str] = None,
    media_ids: Optional[List[Union[int, str]]] = None,
    **kwargs: dict
) -> "Status":
    """
    Updates the authenticating user's current status, also known as Tweeting.

    Args:
        tweepy_credentials: Credentials to use for authentication with Tweepy.
        status: Text of the Tweet being created. This field is required
            if media_ids is not present.
        media_ids: A list of Media IDs being attached to the Tweet.
        kwargs: Additional keyword arguments to pass to update_status.
    Returns:
        A Tweepy Status object.

    Example:
        Tweets an update.
        ```python
        from prefect import flow
        from prefect_twitter import TweepyCredentials
        from prefect_twitter.tweets import update_status

        @flow
        def example_update_status_flow():
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
            update_status(tweepy_credentials, status="A Prefect Tweet!")

        example_update_status_flow()
        ```
    """
    logger = get_run_logger()
    logger.info("Updating status")

    if status is None and media_ids is None:
        raise ValueError("One of text or media_ids must be provided")

    api = tweepy_credentials.get_api()
    partial_update = partial(
        api.update_status, status=status, media_ids=media_ids, **kwargs
    )
    status = await to_thread.run_sync(partial_update)
    return status
