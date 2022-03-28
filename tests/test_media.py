from prefect import flow

from prefect_twitter.media import media_upload


def test_media_upload(twitter_credentials):
    path = "/path/to/prefection.jpg"

    @flow
    def test_flow():
        media = media_upload(path, twitter_credentials, chunked=False)
        return media

    result = test_flow().result().result()
    assert result["media_id"] == path
    assert result["chunked"] is False
