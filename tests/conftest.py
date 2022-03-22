from unittest.mock import MagicMock

import pytest


class APIMock:
    def media_upload(self, filename, **kwargs):
        return filename

    def update_status(self, status=None, media_ids=None, **kwargs):
        if media_ids:
            return media_ids
        else:
            return status


@pytest.fixture
def tweepy_credentials(monkeypatch):
    credentials_mock = MagicMock()
    credentials_mock.get_api.side_effect = lambda: APIMock()
    return credentials_mock
