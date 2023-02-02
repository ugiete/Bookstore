from django.contrib import admin
from django.contrib.auth import get_user_model
import django.contrib.auth.admin as a

from .forms import UserChangeForm, UserCreationForm

UserModel = get_user_model()

class UserAdmin(a.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserModel
    list_display = [
        'email',
        'username',
        'is_superuser'
    ]

admin.site.register(UserModel, UserAdmin)