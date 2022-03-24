from django import forms

#There is two forms
#1) ModelForm - forms based on model fields
#2) Form - simple form

class LoginForm(forms.Form):
    username = forms.CharField()
    login = forms.CharField(widget=forms.PasswordInput)


