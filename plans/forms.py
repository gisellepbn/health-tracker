from .models import Profile
from django.forms import ModelForm, PasswordInput, FileInput


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'username', 'password', 'picture']
        labels = {
            'name': '', 'username':'', 'password':'',
        }
        help_texts = {
            "username": None,
        }

        widgets = {
            'password': PasswordInput(),
            'picture': FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input', 'placeholder': 'Full Name', 'name': 'name', 'autofocus': True})
        self.fields['username'].widget.attrs.update({'class':'input', 'placeholder': 'Username', 'name': 'username'})
        self.fields['password'].widget.attrs.update({'class':'input', 'placeholder': 'Password', 'name': 'password'})
        self.fields['picture'].widget.attrs.update({'id':'profile_picture', 'name': 'picture'})