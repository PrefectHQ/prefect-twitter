import pytest

from prefect import flow
from prefect_twitter.tweets import update_status


def test_update_status(tweepy_credentials):
    status = "tweeting prefection!"

    @flow
    def test_flow():
        media = update_status(tweepy_credentials, status=status)
        return media
    
    assert test_flow().result().result() == status


def test_update_status_missing(tweepy_credentials):
    @flow
    def test_flow():
        media = update_status(tweepy_credentials)
        return media

    with pytest.raises(ValueError):
        test_flow().result().result()


def test_update_status_media(tweepy_credentials):
    media_ids = [1, 2, 3]

    @flow
    def test_flow():
        media = update_status(tweepy_credentials, media_ids=media_ids)
        return media

    assert test_flow().result().result() == media_ids
