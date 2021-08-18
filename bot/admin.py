from django.contrib import admin
from django import forms
from bot.models import User, UserActionLog, StaticText
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
        search_fields = ['description', 'content']
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

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('description', 'name')
        return self.readonly_fields

#@admin.register(StaticText)
#class StaticTextAdmin(admin.ModelAdmin):
#    list_display = ['name', 'description', 'content']
#    search_fields = ['description', 'content']
#    fieldsets = (
#        (None, {
#            "fields": ('name', 'description', 'content')
#        }
#        ),
#    )
#
#    def get_readonly_fields(self, request, obj=None):
#        if obj:  # editing an existing object
#            return self.readonly_fields + ('name', 'description')
#        return self.readonly_fields
