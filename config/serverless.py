from helio.settings import *

# websites/manage.py runserver --settings=config.local
print ('>>>>>>>>> DEPLOY IN SERVERLESS')
INSTALLED_APPS += ["django_s3_sqlite", "django_s3_storage"]
ALLOWED_HOSTS += ["https://4p35ue6l4i.execute-api.ap-northeast-1.amazonaws.com/dev"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django_s3_sqlite",
#         "NAME": "sqlite_zappa.db",
#         "BUCKET": "zappa-5ntulw84i",
#     }
# }
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

S3_BUCKET_NAME = "zappa-media-serve"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET_NAME

# to serve the static files from your s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % S3_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN



print ("==========================")
