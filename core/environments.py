from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = bool(int(environ.get('DEBUG', 0)))
ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', ' ').split()

# master database
NAME = environ.get('POSTGRES_DATABASE')
USER = environ.get('POSTGRES_USERNAME')
PASSWORD = environ.get('POSTGRES_PASSWORD')
HOST = environ.get('POSTGRES_HOST')
PORT = environ.get('POSTGRES_PORT')

# slave database
NAME_SALVE_1 = environ.get('POSTGRES_DATABASE_SALVE_1')
USER_SALVE_1 = environ.get('POSTGRES_USERNAME_SALVE_1')
PASSWORD_SALVE_1 = environ.get('POSTGRES_PASSWORD_SALVE_1')
HOST_SALVE_1 = environ.get('POSTGRES_HOST_SALVE_1')
PORT_SALVE_1 = environ.get('POSTGRES_PORT_SALVE_1')
