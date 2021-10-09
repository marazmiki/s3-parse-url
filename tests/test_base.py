import pytest

from s3_parse_url.exceptions import StorageAlreadyRegistered
from s3_parse_url.storages import register_storage
from s3_parse_url.storages.amazon import AmazonS3


def test_register_storage_twice():
    with pytest.raises(StorageAlreadyRegistered):
        register_storage("s3", AmazonS3)
