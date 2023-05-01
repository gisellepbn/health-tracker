from .models import Profile
from django.forms import ModelForm, PasswordInput


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'username', 'password', 'profile_picture']
        labels = {
            'name': '', 'username':'', 'password':'', 'profile_picture': 'Profile Picture',
        }
        help_texts = {
            "username": None,
        }

        widgets = {
            'password': PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input', 'placeholder': 'Full Name', 'autofocus': True})
        self.fields['username'].widget.attrs.update({'class':'input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class':'input', 'placeholder': 'Password'})
        self.fields['profile_picture'].widget.attrs.update({'id':'picture'})