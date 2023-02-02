from django.contrib.auth import get_user_model, forms

class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username'
        )

class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username'
        )