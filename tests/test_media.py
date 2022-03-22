from prefect import flow

from prefect_twitter.media import media_upload


def test_media_upload(tweepy_credentials):
    path = "/path/to/prefection.jpg"

    @flow
    def test_flow():
        media = media_upload(path, tweepy_credentials, chunked=False)
        return media

    assert test_flow().result().result() == path
