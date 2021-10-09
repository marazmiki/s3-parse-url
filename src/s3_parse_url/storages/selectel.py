from s3_parse_url.base import S3DataSource


class SelectelStorage(S3DataSource):
    allowed_schemas = ["selectel"]
    default_region = "ru-1"
    default_endpoint = "https://s3.selcdn.ru"
