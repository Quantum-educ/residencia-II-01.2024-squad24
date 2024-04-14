from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Profile


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    accept_terms = forms.BooleanField(required=True)

    class Meta:
        model = Student
        fields = [
            'username',
            'email',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError('As senhas devem coincidir.')
        if len(password) < 8:
            raise ValidationError('A senha deve possui no mínimo 8 caracteres')
        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)
        student.set_password(self.cleaned_data['password'])
        if commit:
            profile = Profile.objects.create()
            student.profile = profile
            student.save()
        return student
