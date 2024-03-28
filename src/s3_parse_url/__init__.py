from urllib.parse import urlparse

from s3_parse_url.base import INSECURE_SCHEME_SUFFIX, S3DataSource
from s3_parse_url.exceptions import UnsupportedStorage
from s3_parse_url.storages import SUPPORTED_STORAGES

__version__ = "0.4.0"
__all__ = ["parse_s3_dsn", "parse_s3_url", "UnsupportedStorage"]


def parse_s3_dsn(dsn: str) -> S3DataSource:
    """
    Parses a datasource string to a dict of arguments compatible with
    """
    insecure_suffix = INSECURE_SCHEME_SUFFIX
    try:
        scheme = urlparse(dsn).scheme.lower()
        if scheme.endswith(insecure_suffix):
            scheme = scheme[:-len(insecure_suffix)]
        cls = SUPPORTED_STORAGES[scheme]
    except (AttributeError,
            KeyError):
        raise UnsupportedStorage()
    else:
        return cls(dsn)


parse_s3_url = parse_s3_dsn
