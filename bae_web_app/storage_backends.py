from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django_tenants.utils import parse_tenant_config_path


class BackendS3Storage(S3Boto3Storage):
    auto_create_bucket = True
    default_acl = 'public-read'
    bucket_acl = default_acl

    @property  # not cached like in parent of S3Boto3Storage class
    def location(self):
        _location = parse_tenant_config_path(
            settings.AWS_PRIVATE_MEDIA_LOCATION) # here you can just put '%s'
        return _location
