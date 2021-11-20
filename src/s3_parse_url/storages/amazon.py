from typing import Optional
from s3_parse_url.base import S3DataSource


class AmazonS3(S3DataSource):
    allowed_schemas = ["s3"]
    default_region = "us-east-1"
    amazon_s3_domains = (
        ".s3.amazonaws.com",
        ".s3.aws.amazon.com",
    )

    def _is_amazon_host(self):
        return all((
            self._raw_bits.hostname,
            self._raw_bits.hostname.lower().endswith(self.amazon_s3_domains)
        ))

    def _strip_amazon_prefix(self):
        for d in self.amazon_s3_domains:
            if not self._raw_bits.hostname.endswith(d):
                continue
            return self._raw_bits.hostname[:-len(d)]

    def _is_host_given(self):
        if self._is_amazon_host():
            return False
        return super()._is_host_given()

    def _parse_bucket_name(self) -> Optional[str]:
        _parent = super()._parse_bucket_name()
        if self._is_amazon_host():
            return self._strip_amazon_prefix()
        return _parent
