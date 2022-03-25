import pytest
from prefect import flow

from prefect_twitter.tweets import update_status


def test_update_status(twitter_credentials):
    status = "tweeting prefection!"

    @flow
    def test_flow():
        media = update_status(twitter_credentials, status=status)
        return media

    assert test_flow().result().result() == status


def test_update_status_missing(twitter_credentials):
    @flow
    def test_flow():
        media = update_status(twitter_credentials)
        return media

    with pytest.raises(ValueError, match="One of text or media_ids"):
        test_flow().result().result()


def test_update_status_media(twitter_credentials):
    media_ids = [1, 2, 3]

    @flow
    def test_flow():
        media = update_status(twitter_credentials, media_ids=media_ids)
        return media

    assert test_flow().result().result() == media_ids[0]
