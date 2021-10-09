from typing import List, Optional
from urllib.parse import parse_qs, urlparse

from s3_parse_url.exceptions import InsecureNotAllowed, UnsupportedStorage

SECURE_HTTP_SCHEME = "https"
INSECURE_HTTP_SCHEME = "http"
INSECURE_SCHEME_SUFFIX = "+insecure"


class S3DataSource:
    allowed_schemas: List[str] = ["s3"]
    default_endpoint: str = None
    default_region: str = None
    allow_insecure_scheme: bool = False
    region_param_name: str = "region"

    def __init__(self, dsn: str):
        self._dsn = dsn
        self._raw_bits = None
        self._parsed_bits = {}
        self._parse()

    def __str__(self):
        return self._dsn

    @property
    def endpoint_url(self) -> Optional[str]:
        return self._parsed_bits["endpoint_url"]

    @property
    def bucket_name(self) -> str:
        return self._parsed_bits["bucket_name"]

    @property
    def region(self) -> str:
        return self._parsed_bits["region"]

    @property
    def access_key_id(self) -> str:
        return self._parsed_bits["aws_access_key_id"]

    @property
    def secret_access_key(self) -> str:
        return self._parsed_bits["aws_secret_access_key"]

    @property
    def key(self) -> str:
        return self._parsed_bits["key"]

    def _parse(self):
        self._raw_bits = urlparse(self._dsn, allow_fragments=False)
        self._check_if_compatible()
        self._parsed_bits.update(**{
            "aws_secret_access_key": self._parse_secret_access_key(),
            "aws_access_key_id": self._parse_access_key_id(),
            "endpoint_url": self._parse_endpoint_url(),
            "bucket_name": self._parse_bucket_name(),
            "region": self._parse_region_name(),
            "key": self._parse_key(),
        })

    def _parse_access_key_id(self):
        return self._raw_bits.username

    def _parse_secret_access_key(self):
        return self._raw_bits.password

    def _is_host_given(self):
        "Checks if in the DSN there is an explicitly given domain name"
        return any((
            self._raw_bits.port is not None,
            self._raw_bits.hostname.count(".") > 0
        ))

    def _parse_endpoint_url(self):
        if not self._is_host_given():
            return self.default_endpoint
        schema_prefix = self._parse_schema_prefix()
        host, port = self._raw_bits.hostname, self._raw_bits.port
        if port:
            return schema_prefix + host + ":" + str(port) + "/"
        else:
            return schema_prefix + host + "/"

    def _parse_region_name(self) -> str:
        region = parse_qs(self._raw_bits.query).get(self.region_param_name)
        if region and region[0]:
            return region[0]
        else:
            return self.default_region

    def _parse_bucket_name(self) -> str:
        if self._is_host_given():
            bucket_name, *key_bits = self._raw_bits.path.lstrip("/").split("/")
            return bucket_name
        else:
            return self._raw_bits.hostname

    def _parse_key(self) -> str:
        key = self._raw_bits.path.lstrip("/")
        return key

    def _parse_schema_prefix(self) -> str:
        if self.allow_insecure_scheme:
            schema = (INSECURE_HTTP_SCHEME
                      if self._raw_bits.scheme.endswith(INSECURE_SCHEME_SUFFIX)
                      else SECURE_HTTP_SCHEME)
        else:
            schema = SECURE_HTTP_SCHEME
        return schema + "://"

    def _check_if_compatible(self):
        scheme = self._raw_bits.scheme
        if not self.allowed_schemas:
            return
        if not scheme:
            raise UnsupportedStorage("Unable to detect schema")

        canonical_scheme = scheme.lower()
        scheme_is_insecure = scheme.endswith(INSECURE_SCHEME_SUFFIX)

        if scheme_is_insecure:
            canonical_scheme = canonical_scheme[:-len(INSECURE_SCHEME_SUFFIX)]
            if not self.allow_insecure_scheme:
                raise InsecureNotAllowed("Insecure interaction does not "
                                         "allowed for the backend")
        if canonical_scheme not in self.allowed_schemas:
            raise UnsupportedStorage("Unsupported schema " + scheme +
                                     " for the backend")
