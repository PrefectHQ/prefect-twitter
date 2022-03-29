from unittest.mock import MagicMock

import pytest


class APIMock:
    def media_upload(self, filename, **kwargs):
        return MagicMock(media_id={"media_id": filename, **kwargs})

    def update_status(self, status=None, media_ids=None, **kwargs):
        if media_ids:
            return MagicMock(id=media_ids[0])
        else:
            return MagicMock(id=status)

    def get_status(self, status_id=None, **kwargs):
        return status_id

    def get_media_upload_status(self, media_id=None, **kwargs):
        return media_id


@pytest.fixture
def twitter_credentials(monkeypatch):
    credentials_mock = MagicMock()
    credentials_mock.get_api.side_effect = APIMock
    return credentials_mock
