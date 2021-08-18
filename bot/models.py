from django.db import models
from bot.models_utils import extract_user_data_from_update


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="Id")
    username = models.CharField(max_length=32, null=True, blank=True, verbose_name="Ник")
    first_name = models.CharField(max_length=256, verbose_name="Имя")
    last_name = models.CharField(max_length=256, null=True, blank=True, verbose_name="Фамилия")
    language_code = models.CharField(max_length=8, null=True, blank=True, help_text="Telegram client's lang", verbose_name="Язык")

    is_blocked_bot = models.BooleanField(default=False, verbose_name="Заблокировал бота")
    is_banned = models.BooleanField(default=False, verbose_name="В бане")

    is_admin = models.BooleanField(default=False, verbose_name="Админ")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлен")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    @classmethod
    def get_user(cls, update):
        data = extract_user_data_from_update(update)
        u, created = cls.objects.update_or_create(user_id=data["user_id"], defaults=data)
        return u, created

    @classmethod
    def get_user_by_username_or_user_id(cls, string):
        username = str(string).replace("@", "").strip().lower()
        if username.isdigit():  # user_id
            return cls.objects.filter(user_id=int(username)).first()
        return cls.objects.filter(username__iexact=username).first()


class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    action = models.CharField(max_length=128, verbose_name="Действие")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время")

    def __str__(self):
        return f"Пользователь: {self.user}, отправил: {self.action}, в {self.created_at.strftime('(%H:%M, %d %B %Y)')}"


class StaticText(models.Model):
    name = models.CharField(max_length=256, primary_key=True, verbose_name="Имя")
    description = models.CharField(max_length=256, verbose_name="Описание")
    content = models.TextField(max_length=4096, verbose_name="Текст")

    @classmethod
    def load_text(cls, name):
        return cls.objects.filter(name=name).first().content

    @classmethod
    def load_all(cls):
        return cls.objects.filter().all()
