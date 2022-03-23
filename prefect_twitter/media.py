"""This is a module for interacting with Twitter media"""

from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Union

from anyio import to_thread
from prefect import get_run_logger, task

if TYPE_CHECKING:
    from io import IOBase

    from prefect_twitter import TwitterCredentials


@task
async def media_upload(
    filename: Union[Path, str],
    twitter_credentials: "TwitterCredentials",
    file: "IOBase" = None,
    chunked: bool = None,
    **kwargs: dict
) -> int:
    """
    Use this to upload media to Twitter. Chunked media upload
    is automatically used for videos.

    Args:
        filename: The filename of the image to upload.
            This will automatically be opened unless file is specified.
        twitter_credentials: Credentials to use for authentication with Tweepy.
        file: A file object, which will be used instead of opening filename.
            Note, filename is still required, for MIME type detection and
            to use as a form field in the POST data.
        chunked: Whether or not to use chunked media upload.
            Videos use chunked upload regardless of this parameter.
        kwargs: Additional keyword arguments to pass to media_upload.
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

        example_update_status_flow()
        ```
    """
    logger = get_run_logger()
    logger.info("Uploading media named %s", filename)

    api = twitter_credentials.get_api()
    partial_media = partial(
        api.media_upload, filename=filename, file=file, chunked=chunked, **kwargs
    )
    media = await to_thread.run_sync(partial_media)
    media_id = media.media_id
    return media_id
