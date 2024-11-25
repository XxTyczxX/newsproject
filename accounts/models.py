from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # 各項目を定義する（ユーザ名、パスワード、、、）
    pass