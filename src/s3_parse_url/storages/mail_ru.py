from s3_parse_url.base import S3DataSource


class IceBox(S3DataSource):
    default_region = "ru-msk"
    default_endpoint = "https://ib.bizmrg.com"
    allowed_schemas = ["mailru+ice"]


class HotBox(S3DataSource):
    default_region = "ru-msk"
    default_endpoint = "https://hb.bizmrg.com"
    allowed_schemas = ["mailru", "mailru+hot"]
