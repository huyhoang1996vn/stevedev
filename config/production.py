from helio.settings import *

# websites/manage.py runserver --settings=config.local
print ('>>>>>>>>> DEPLOY IN LOCAL')

DATABASES = {
    'default': {
        'NAME': 'django3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'huyhoang@123',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


print ("==========================")
