import pytest
from prefect import flow

from prefect_twitter.tweets import get_status, update_status


def test_update_status(twitter_credentials):
    status = "tweeting prefection!"

    @flow
    def test_flow():
        status_id = update_status(twitter_credentials, status=status)
        return status_id

    assert test_flow() == status


def test_update_status_missing(twitter_credentials):
    @flow
    def test_flow():
        status_id = update_status(twitter_credentials)
        return status_id

    with pytest.raises(ValueError, match="One of text or media_ids"):
        test_flow()


def test_update_status_media(twitter_credentials):
    media_ids = [1, 2, 3]

    @flow
    def test_flow():
        status_id = update_status(twitter_credentials, media_ids=media_ids)
        return status_id

    assert test_flow() == media_ids[0]


def test_get_status(twitter_credentials):
    status_id = 42

    @flow
    def test_flow():
        status = get_status(status_id, twitter_credentials)
        return status

    assert test_flow() == status_id
