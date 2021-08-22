from django.db import models
from django.db.utils import IntegrityError
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

    def __str__(self):
        return f"{self.description}"

    @classmethod
    def load_text(cls, name):
        text = cls.objects.filter(name=name).first()
        if text is not None:
            return text.content
        else:
            return f"ERROR NO TEXT FOR THIS MESSAGE '{name}'"

    @classmethod
    def load_all(cls):
        return cls.objects.filter().all()

    @classmethod
    def create(cls, name, description, content):
        try:
            obj, _ = cls.objects.get_or_create(name=name, defaults={"description": description, "content": content})
            return obj.content
        except IntegrityError:
            pass


class RentObject(models.Model):
    id = models.AutoField(primary_key=True)
    type_choices = [('ka', 'Каяк'), ('su', 'SUP'), ('wi', 'Wind SUP')]
    advanced_type_choices = [
        ('Каяк', (
            ('op', 'Открытый'),
            ('cl', 'Закрытый'),
                )
        ),
    ]
    rent_type = models.CharField(max_length=2, choices=type_choices, verbose_name='Вид')
    advanced_rent_type = models.CharField(max_length=2, choices=advanced_type_choices, verbose_name='Тип')
    name = models.CharField(max_length=128, verbose_name='Имя')
    amount = models.IntegerField(default=1, verbose_name="Количество")
    capacity = models.IntegerField(default=1, verbose_name="Взрослый")
    child_capacity = models.IntegerField(default=0, verbose_name="Ребенок")
    hour_price = models.IntegerField(default=600, verbose_name="Час")
    four_hour_price = models.IntegerField(default=1300, verbose_name="4 часа")
    daytime_price = models.IntegerField(default=1600, verbose_name="День")
    all_day_price = models.IntegerField(default=2000, verbose_name="Сутки")
    description = models.TextField(max_length=4096, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name="Показывать")

    @classmethod
    def get_all_type_available(cls, rent_type):
        return cls.objects.filter(rent_type=rent_type, is_active=True).all()

    @classmethod
    def get_by_id(cls, obj_id):
        return cls.objects.filter(id=obj_id, is_active=True).first()

    def __str__(self):
        return self.name
