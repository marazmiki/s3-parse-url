from s3_parse_url.base import S3DataSource

# See https://docs.min.io/docs/aws-cli-with-minio.html
#
# A notable thing: according to the docs, the default region
# should be "us-east-1"


class Minio(S3DataSource):
    allowed_schemas = ["minio"]
    default_region = "us-east-1"
    allow_insecure_scheme = True

    def _parse_endpoint_url(self) -> str:
        endpoint_url = super()._parse_endpoint_url()
        return endpoint_url
