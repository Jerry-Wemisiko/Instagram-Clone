from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Image,Comment

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model =User
        fields = ['username','full_name','email','password1','password2',]

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','full_name', 'bio']        


class uploadImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['profile', 'likes', 'comments']

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Comment here'
    