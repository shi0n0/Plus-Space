from datetime import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# カスタムユーザーマネージャーを定義
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("ユーザー名は必須です")
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # ユーザー名を正規化（任意）
        username = self.normalize_username(username)
        
        # ユーザーオブジェクトを作成
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('スーパーユーザーはis_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザーはis_superuser=Trueである必要があります。')

        return self.create_user(username, password, **extra_fields)

# カスタムユーザーモデルを定義
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # ユーザー名（必須）
    username = models.CharField(max_length=150, unique=True)
    # その他のカスタムフィールドを追加する場合はここに記述する

    # スーパーユーザーとして設定する権限（必須）
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # ユーザーマネージャーを設定
    objects = CustomUserManager()

    # ユーザー名を識別するフィールドを設定
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username