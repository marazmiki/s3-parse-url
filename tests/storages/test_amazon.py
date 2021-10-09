import pytest

from s3_parse_url import parse_s3_dsn
from s3_parse_url.storages.amazon import AmazonS3


@pytest.mark.parametrize(
    argnames="dsn, expected_values",
    argvalues=[
        ("s3://my-bucket.s3.amazonaws.com", {"endpoint_url": None}),
        ("s3://my-bucket.s3.amazonaws.com", {"bucket_name": "my-bucket"}),
        ("s3://my-bucket.s3.amazonaws.com/", {"endpoint_url": None}),
        ("s3://my-bucket.s3.amazonaws.com/", {"bucket_name": "my-bucket"}),
        ("s3://xxx:yyy@my-bucket.s3.amazonaws.com/", {"endpoint_url": None}),
        ("s3://xxx:yyy@my-bucket.s3.amazonaws.com/", {
            "bucket_name": "my-bucket"
        }),
        ("s3://xxx:yyy@my-bucket.s3.amazonaws.com/", {"access_key_id": "xxx"}),
        ("s3://xxx:yyy@my-bucket.s3.amazonaws.com/", {
            "secret_access_key": "yyy"
        }),
        ("s3://my-bucket.s3.amazonaws.com/my/key_#1.txt", {
            "bucket_name": "my-bucket",
            "key": "my/key_#1.txt",
        }),
        ("s3://xxx:yyy@custom.domain.com/", {
            "endpoint_url": "https://custom.domain.com/"
        }),
    ],
)
def test_amazon_specified_parse_url(dsn, expected_values):
    for field, expected_value in expected_values.items():
        assert getattr(parse_s3_dsn(dsn), field) == expected_value, field


def test_just_for_coverage():
    dsn = AmazonS3("s3://bucket-not")
    dsn._strip_amazon_prefix()
