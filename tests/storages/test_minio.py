import pytest

from s3_parse_url import parse_s3_dsn
from s3_parse_url.exceptions import InsecureNotAllowed
from s3_parse_url.storages.minio import Minio


@pytest.mark.parametrize(
    argnames="dsn, field, expected_value",
    argvalues=[
        ("minio://xxx:yyy@example.com/bucket?region", "endpoint_url",
         "https://example.com/"),
        ("minio://xxx:yyy@example.com/bucket?region", "region", "us-east-1"),
        ("minio://xxx:yyy@example.com/bucket?region", "bucket_name", "bucket"),
        ("minio://xxx:yyy@example.com/bucket?region", "access_key_id", "xxx"),
        ("minio://xxx:yyy@example.com/bucket?region", "secret_access_key",
         "yyy"),
        ("minio://xxx:yyy@example.com:9000/bucket?region", "endpoint_url",
         "https://example.com:9000/"),
        ("minio+insecure://xxx:yyy@example.com/bucket?region", "endpoint_url",
         "http://example.com/"),
        ("minio+insecure://xxx:yyy@example.com:9123/bucket?region",
         "endpoint_url", "http://example.com:9123/"),


    ]
)
def test_minio(dsn, field, expected_value):
    assert getattr(parse_s3_dsn(dsn), field) == expected_value


def test_minio_insecure_false(monkeypatch):
    monkeypatch.setattr(Minio, "allow_insecure_scheme", False)
    parsed = parse_s3_dsn("minio://xxx:yyy@example.com/bucket?region")
    assert parsed.endpoint_url == "https://example.com/"


def test_minio_insecure_false_validation(monkeypatch):
    monkeypatch.setattr(Minio, "allow_insecure_scheme", False)
    with pytest.raises(InsecureNotAllowed):
        parse_s3_dsn("minio+insecure://xxx:yyy@example.com/bucket")
