class S3ParseException(Exception):
    pass


class UnsupportedStorage(S3ParseException):
    pass


class StorageAlreadyRegistered(S3ParseException):
    pass


class InsecureNotAllowed(S3ParseException):
    pass
