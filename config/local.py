from helio.settings import *

# websites/manage.py runserver --settings=config.local
print ('>>>>>>>>> DEPLOY IN LOCAL')

DATABASES = {
    'default': {
        'NAME': 'django3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


print ("==========================")
