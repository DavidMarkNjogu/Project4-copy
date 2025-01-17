from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile




class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']  # Add other fields as needed
