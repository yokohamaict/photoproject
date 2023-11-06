from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # カスタムユーザテーブルに登録するためのフォーム
        model = CustomUser
        # 入力欄に表示するもの(テーブルの列名で指定)
        fields = ('username', 'email', 'password1', 'password2')