"""This is a module for interacting with Twitter media"""

from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Union

from anyio import to_thread
from prefect import get_run_logger, task

if TYPE_CHECKING:
    from io import IOBase

    from tweepy import Media

    from prefect_twitter import TwitterCredentials


@task
async def media_upload(
    filename: Union[Path, str],
    twitter_credentials: "TwitterCredentials",
    file: Optional["IOBase"] = None,
    chunked: bool = False,
    **kwargs: dict
) -> int:
    """
    Uploads media to Twitter. Chunked media upload
    is automatically used for videos.

    Args:
        filename: The filename of the image to upload.
            This field is used for MIME type detection.
        twitter_credentials: Credentials to use for authentication with Twitter.
        file: A file object to upload. If not specified, this task will attempt to
            locate and upload a file with the name specified in filename.
        chunked: Whether or not to use chunked media upload.
            Videos use chunked upload regardless of this parameter.
        kwargs: Additional keyword arguments to pass to
            [media_upload](https://docs.tweepy.org/en/stable/api.html#tweepy.API.media_upload).
    Returns:
        The media ID.

    Example:
        Uploads an image from a file path to Twitter.
        ```python
        from prefect import flow
        from prefect_twitter import TwitterCredentials
        from prefect_twitter.media import media_upload

        @flow
        def example_media_upload_flow():
            twitter_credentials = TwitterCredentials(
                consumer_key="consumer_key",
                consumer_secret="consumer_secret",
                access_token="access_token",
                access_token_secret="access_token_secret"
            )
            media_id = media_upload("/path/to/prefection.jpg", twitter_credentials)
            return media_id

        example_media_upload_flow()
        ```
    """  # noqa
    logger = get_run_logger()
    logger.info("Uploading media named %s", filename)

    api = twitter_credentials.get_api()
    partial_media = partial(
        api.media_upload, filename=filename, file=file, chunked=chunked, **kwargs
    )
    media = await to_thread.run_sync(partial_media)
    media_id = media.media_id
    return media_id


@task
async def get_media_upload_status(
    media_id: int, twitter_credentials: "TwitterCredentials"
) -> "Media":
    """
    Check on the progress of a chunked media upload. If the upload has succeeded,
    it's safe to create a Tweet with this media_id.

    Args:
        media_id: The ID of the media to check.
        twitter_credentials: Credentials to use for authentication with Twitter.

    Returns:
        The Media object.

    Example:
        Tweets an update with just text.
        ```python
        from prefect import flow
        from prefect_twitter import TwitterCredentials
        from prefect_twitter.media import get_media_upload_status

        @flow
        def example_get_media_upload_status_flow():
            twitter_credentials = TwitterCredentials(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            media_id = 1443668738906234883
            media = get_media_upload_status(media_id, twitter_credentials)
            return media

        example_get_media_upload_status_flow()
        ```
    """
    api = twitter_credentials.get_api()
    partial_get = partial(api.get_media_upload_status, media_id)
    media = await to_thread.run_sync(partial_get)
    return media
