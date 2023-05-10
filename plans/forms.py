from .models import Profile, Plan
from django.forms import ModelForm, PasswordInput, FileInput, Select


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



class GoalForm(ModelForm):

    class Meta:
        model= Plan
        fields= ['parameter', 'goal', 'unit']
       
         
    
    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)

        self.fields['parameter'].widget.attrs.update({'class':'input parameter-input', 'name': 'category'})
        self.fields['goal'].widget.attrs.update({'class':'input', 'name': 'goal'})
        self.fields['unit'].widget.attrs.update({'class':'input', 'name': 'unit'})



class ProgressForm(ModelForm):

    class Meta:
        model= Plan
        fields= ['parameter', 'progress', 'unit']
       
         
    
    def __init__(self, *args, **kwargs):
        super(ProgressForm, self).__init__(*args, **kwargs)

        self.fields['parameter'].widget.attrs.update({'class':'input parameter-input', 'name': 'category'})
        self.fields['progress'].widget.attrs.update({'class':'input', 'name': 'progress'})
        self.fields['unit'].widget.attrs.update({'class':'input', 'name': 'unit'})