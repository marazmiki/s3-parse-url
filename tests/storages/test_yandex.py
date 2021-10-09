from s3_parse_url import parse_s3_dsn


def test_yandex():
    parsed = parse_s3_dsn("yandex://xxx:yyy@my-bucket/")
    assert parsed.endpoint_url == "https://storage.yandexcloud.net"
    assert parsed.region == "ru-central1"
