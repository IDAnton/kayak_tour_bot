from django.contrib import admin
from django import forms
from bot.models import User, UserActionLog, StaticText, RentObject
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 'username', 'first_name', 'last_name',
        'language_code',
        'created_at', 'updated_at', "is_blocked_bot",
    ]
    list_filter = ["is_blocked_bot"]
    search_fields = ('username', 'user_id')


@admin.register(UserActionLog)
class UserActionLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'created_at']


class StaticTextForm(forms.ModelForm):
    content = forms.CharField(widget=EmojiPickerTextareaAdmin)

    class Meta:
        model = StaticText
        list_display = ['name', 'description', 'content']
        fields = ['name', 'description', 'content']
        fieldsets = (
                    (None, {
                        "fields": ('name', 'description', 'content')
                    }
                    ),
                )


@admin.register(StaticText)
class StaticTextAdmin(admin.ModelAdmin):
    form = StaticTextForm
    search_fields = ['description', 'content']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('description', 'name')
        return self.readonly_fields


@admin.register(RentObject)
class RentObjectAdmin(admin.ModelAdmin):
    #form = RentObjectForm
    search_fields = ['name', 'description', 'rent_type']
    fieldsets = (
        (None, {
            "fields": ('rent_type', 'advanced_rent_type', 'name', 'amount')
        }
         ),
        ('Вместимтость', {
            'fields': (('capacity', 'child_capacity'),)
        }),
        ('Цена', {
            'fields': (('hour_price', 'four_hour_price', 'daytime_price', 'all_day_price'),)
        }),
        (None, {
            'fields': ('description', 'is_active')
        }),
    )
