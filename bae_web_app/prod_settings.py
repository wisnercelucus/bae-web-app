from .settings import *
import dj_database_url
#import django_heroku

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['bae-app.herokuapp.com']

#DATABASES['default'] = dj_database_url.config()

#MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



#config = locals()
#django_heroku.settings(config, databases=False, staticfiles=False)

#conn_max_age = config.get('CONN_MAX_AGE', 600)

#config['DATABASES'] = {
#	'default': dj_database_url.parse(
#	os.environ['DATABASE_URL'],
#	engine='django_tenants.postgresql_backend',
#	conn_max_age=conn_max_age,
#	ssl_require=True
#	)
#}

DATABASES['default'] = dj_database_url.config()

#Celery settings
#CELERY_BROKER_URL = 'redis://h:p51ade22e411702848e6a865d44b71d789f5cdc4f316102305d831792055e89a1@ec2-34-202-225-162.compute-1.amazonaws.com:26359'
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_TASK_SERIALIZER = 'json'


AWS_ACCESS_KEY_ID =  os.environ.get('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bae-bukect'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_LOCATION = STATIC_URL
DEFAULT_FILE_STORAGE = 'bae_web_app.storage_backends.BackendS3Storage'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
