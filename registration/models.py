from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    # USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'
