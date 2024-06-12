from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = bool(int(environ.get('DEBUG', 0)))
ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', ' ').split()
