from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    # confirm password
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("Passwords don't match, please try again.")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender',)
