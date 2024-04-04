from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean_validate_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('As senhas devem coincidir.')
        if len(password) < 8:
            raise ValidationError('A senha deve possui no mínimo 8 caracteres')
        return password
           

