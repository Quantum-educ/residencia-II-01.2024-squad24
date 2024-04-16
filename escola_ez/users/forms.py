from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import Student, Profile


class StudentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    accept_terms = forms.BooleanField(required=True)

    class Meta:
        model = Student
        fields = [
            'username',
            'email',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if Student.objects.filter(email=email).exists():
            raise ValidationError('O email fornecido já está cadastrado.')
        if len(password) < 8:
            raise ValidationError('A senha deve possuir no mínimo 8 caracteres.')
        if password != confirm_password:
            raise ValidationError('As senhas devem coincidir.')
        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)
        student.set_password(self.cleaned_data['password'])
        if commit:
            profile = Profile.objects.create()
            student.profile = profile
            student.save()
        return student


class StudentSignInForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Nome de usuário ou senha incorretos.')
        cleaned_data['user'] = user
        return cleaned_data
