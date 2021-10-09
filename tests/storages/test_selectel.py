from s3_parse_url import parse_s3_dsn


def test_selectel():
    parsed = parse_s3_dsn("selectel://xxx:yyy@my-bucket/")
    assert parsed.endpoint_url == "https://s3.selcdn.ru"
    assert parsed.region == "ru-1"
