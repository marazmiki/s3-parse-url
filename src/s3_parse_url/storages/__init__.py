from s3_parse_url.exceptions import StorageAlreadyRegistered
from s3_parse_url.storages.amazon import AmazonS3
from s3_parse_url.storages.mail_ru import HotBox, IceBox
from s3_parse_url.storages.minio import Minio
from s3_parse_url.storages.selectel import SelectelStorage
from s3_parse_url.storages.yandex import YandexCloud

SUPPORTED_STORAGES = {}


def register_storage(schema: str, cls):
    if schema in SUPPORTED_STORAGES:
        raise StorageAlreadyRegistered("Schema registered")
    SUPPORTED_STORAGES[schema] = cls


register_storage("s3", AmazonS3)
register_storage("selectel", SelectelStorage)
register_storage("mailru", HotBox)
register_storage("mailru+hot", HotBox)
register_storage("mailru+ice", IceBox)
register_storage("minio", Minio)
register_storage("yandex", YandexCloud)
