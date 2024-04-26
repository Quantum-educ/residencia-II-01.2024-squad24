from django.contrib.auth.backends import ModelBackend
from .models import Student


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Student.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
