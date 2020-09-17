from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'  # stores files under directory `static/` in S3 bucket


class MediaStorage(S3Boto3Storage):
    location = 'media'  # stores files under directory `media/` in S3 bucket
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False