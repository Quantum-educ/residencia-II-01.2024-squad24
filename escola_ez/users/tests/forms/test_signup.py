from django.test import TestCase
from users.forms import StudentSignUpForm


class TestSignUpForm(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.valid_data = {
            'username': 'user',
            'email': 'user@email.com',
            'password': 'password',
            'confirm_password': 'password',
            'accept_terms': True,
        }
    
    def _change_valid_data(self, key: str, value: str) -> dict:
        return {k: value if k == key else v for k, v in self.valid_data.items()}
    
    def test_valid_form(self):
        form = StudentSignUpForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form_blank_username(self):
        invalid_data = self._change_valid_data('username', '')
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_blank_email(self):
        invalid_data = self._change_valid_data('email', '')
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_email_format(self):
        invalid_data = self._change_valid_data('email', 'user.email')
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_short_password(self):
        invalid_data = self._change_valid_data('password', 'shortPw')
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_mismatched_passwords(self):
        invalid_data = self._change_valid_data('confirm_password', 'mismatchedPassword')
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_terms_not_accepted(self):
        invalid_data = self._change_valid_data('accept_terms', False)
        form = StudentSignUpForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_form_email_already_registered(self):
        form = StudentSignUpForm(data=self.valid_data)
        form.save()
        form = StudentSignUpForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
