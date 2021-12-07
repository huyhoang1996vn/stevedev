from helio.settings import *

# websites/manage.py runserver --settings=config.local
print ('>>>>>>>>> DEPLOY IN PROD')

DATABASES = {
    'default': {
        'NAME': 'django3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.getenv('DATABASE_USERNAME', 'postgres'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'huyhoang@123'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': 5432
    }
}


print ("==========================")
