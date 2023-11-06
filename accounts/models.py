from django.db import models
# ユーザテーブルのひな形をインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    用意されているユーザから特に変更しないで使う
    '''
    pass
