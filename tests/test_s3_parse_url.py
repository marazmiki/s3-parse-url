import pytest

from s3_parse_url import parse_s3_dsn
from s3_parse_url.exceptions import UnsupportedStorage
from s3_parse_url.storages.amazon import AmazonS3


@pytest.mark.parametrize(
    argnames="dsn, expected_values",
    argvalues=[
        ("s3://my-bucket", {"endpoint_url": None}),
        ("s3://my-bucket", {"region": "us-east-1"}),
        ("s3://my-bucket", {"bucket_name": "my-bucket"}),
        ("s3://my-bucket?region=us-east-2", {"region": "us-east-2"}),
        ("s3://my-bucket?region=us-east-2", {"bucket_name": "my-bucket"}),
        ("s3://xxx@my-bucket", {"access_key_id": "xxx"}),
        ("s3://xxx@my-bucket", {"bucket_name": "my-bucket"}),
        ("s3://xxx:yyy@my-bucket", {"access_key_id": "xxx"}),
        ("s3://xxx:yyy@my-bucket", {"secret_access_key": "yyy"}),
        ("s3://xxx:yyy@my-bucket", {"bucket_name": "my-bucket"}),
        ("s3://my-bucket/my/key.txt", {"bucket_name": "my-bucket"}),
        ("s3://my-bucket/my/key.txt", {"key": "my/key.txt"}),
        ("s3://my-bucket/my/key_#1.txt", {"bucket_name": "my-bucket"}),
        ("s3://my-bucket/my/key_#1.txt", {"key": "my/key_#1.txt"}),
        ("minio+insecure://my-bucket", {"endpoint_url": None}),
    ],
)
def test_s3_parse_url(dsn, expected_values):
    for field, expected_value in expected_values.items():
        assert getattr(parse_s3_dsn(dsn), field) == expected_value, field


@pytest.mark.parametrize(
    argnames="dsn, expected_values",
    argvalues=[
        ("s3://xxx:yy%2Fy@my-bucket", {"secret_access_key": "yy/y"}),
        ("s3://xxx:yy%23y@my-bucket", {"secret_access_key": "yy#y"}),
        ("s3://xxx:yy%3Ay@my-bucket", {"secret_access_key": "yy:y"}),
    ],
)
def test_s3_parse_url_with_not_format_password(dsn, expected_values):
    for field, expected_value in expected_values.items():
        assert getattr(parse_s3_dsn(dsn), field) == expected_value, field


def test_s3_parse_url_exception():
    with pytest.raises(UnsupportedStorage):
        parse_s3_dsn("wtf://")


def test_str():
    dsn = "s3://my-bucket?region=us-east-2"
    assert str(parse_s3_dsn(dsn)) == dsn


@pytest.mark.parametrize(
    argnames="dsn, allowed_schemas, expect_error",
    argvalues=[
        ("s3://my-bucket", None, False),
        ("s3://my-bucket", ["s3_not"], True),
        ("my-bucket-without-schema", ["s3"], True),
    ]
)
def test_check_if_compatible(monkeypatch, dsn, allowed_schemas, expect_error):
    monkeypatch.setattr(AmazonS3, "allowed_schemas", allowed_schemas)
    if expect_error:
        with pytest.raises(UnsupportedStorage):
            AmazonS3(dsn)
    else:
        AmazonS3(dsn)
