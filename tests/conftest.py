from unittest.mock import MagicMock

import pytest


class APIMock:
    def media_upload(self, filename, **kwargs):
        return MagicMock(media_id=filename)

    def update_status(self, status=None, media_ids=None, **kwargs):
        if media_ids:
            return MagicMock(id=media_ids[0])
        else:
            return MagicMock(id=status)


@pytest.fixture
def twitter_credentials(monkeypatch):
    credentials_mock = MagicMock()
    credentials_mock.get_api.side_effect = lambda: APIMock()
    return credentials_mock
