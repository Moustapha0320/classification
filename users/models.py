from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Manager personnalisé pour UserAccount
class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Modèle utilisateur
class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
