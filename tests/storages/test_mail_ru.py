import pytest

from s3_parse_url import parse_s3_dsn


@pytest.mark.parametrize("schema, expected_endpoint", [
    ("mailru://", "https://hb.bizmrg.com"),
    ("mailru+hot://", "https://hb.bizmrg.com"),
    ("mailru+ice://", "https://ib.bizmrg.com"),
])
def test_mail_ru(schema, expected_endpoint):
    parsed = parse_s3_dsn(schema + "my-bucket/")
    assert parsed.endpoint_url == expected_endpoint
    assert parsed.region == "ru-msk"
