DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'django_launcher_test_db'
DB_USER = 'django_launcher_test_db_user'
DB_PASSWORD = 'django_launcher_test_db_passwd'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

ALLOWED_HOSTS = ['*']  # TODO : WARNING - change this to your domain/sub-domain in prod!
