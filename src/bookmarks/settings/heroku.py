from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#To allow django-admin.py collectstatic to automatically push static files to the S3 bucket:
STATICFILES_STORAGE = 'bookmarks.storage_backends.StaticStorage'

# USER UPLOADED FILES SETTINGS
DEFAULT_FILE_STORAGE = 'bookmarks.storage_backends.MediaStorage'

# AWS S3 SETTINGS
AWS_ACCESS_KEY_ID =  os.environ.get("AWS_ACCESS_KEY_ID", "") # set in heroku env variables
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "") # set in heroku env variables
AWS_STORAGE_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "imarksbucket") # set in heroku as env variable
S3DIRECT_REGION = 'eu-central-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# SORL-THUMBNAIL SPECIFIC << THIS DID NOT HELP
"""
MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + 'media/'
MEDIA_ROOT = MEDIA_URL
STATIC_URL = AWS_S3_CUSTOM_DOMAIN + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
"""

# BROWSER SETTINGS

# Set these to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = True  # False in development, True in production
SESSION_COOKIE_SECURE = True # False in development, True in production

# I SET THIS TO TRUE FOR WHEN EXTERNAL USERS TEST GRIT ALPHA:
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
