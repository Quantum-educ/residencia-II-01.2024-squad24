from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'username',
            'email',
            'password',
            'accept_terms'
        ]
