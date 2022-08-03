from prefect import flow

from prefect_twitter.media import get_media_upload_status, media_upload


def test_media_upload(twitter_credentials):
    path = "/path/to/prefection.jpg"

    @flow
    def test_flow():
        media = media_upload(path, twitter_credentials, chunked=False)
        return media

    result = test_flow()
    assert result["media_id"] == path
    assert result["chunked"] is False


def test_get_media_upload_status(twitter_credentials):
    media_id = 42

    @flow
    def test_flow():
        media = get_media_upload_status(media_id, twitter_credentials)
        return media

    assert test_flow() == media_id
