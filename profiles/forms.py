from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].label = "О себе"
        self.fields['bio'].helper = "Введите информацию..."
        self.fields['avatar'].label = "Аватар"