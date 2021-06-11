from helio.settings import *

# websites/manage.py runserver --settings=config.local
print ('>>>>>>>>> DEPLOY IN LOCAL')

DATABASES = {
    'default': {
        'NAME': 'helio2',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5433
    }
}


print ("==========================")
