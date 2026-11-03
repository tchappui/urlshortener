from .base import *
from .base import env

DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [
    "tch.sh",
    "www.tch.sh",
]

CSRF_TRUSTED_ORIGINS = [
    "https://tch.sh",
    "https://www.tch.sh",
]
