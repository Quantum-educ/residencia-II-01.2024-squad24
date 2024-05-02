from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from users.forms import StudentSignUpForm


class TestSignInView(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('signin')
        cls.data = {
            'username': 'user',
            'email': 'user@email.com',
            'password': 'password',
            'confirm_password': 'password',
            'accept_terms': True,
        }
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_signin_url_exists_at_desired_location(self):
        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, 200)
    
    def test_signin_view_accessible_by_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_signin_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_signin_view_unregistered_student(self):
        self.driver.get(f'{self.live_server_url}/signin/')
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self.driver.find_element('id', 'submit').click()
        self.assertIn(f'{self.live_server_url}/signin/', self.driver.current_url)

    def test_signin_view_student_successfully_authenticated(self):
        self.driver.get(f'{self.live_server_url}/signin/')
        form = StudentSignUpForm(data=self.data)
        form.save()
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self.driver.find_element('id', 'submit').click()
        self.assertIn(f'{self.live_server_url}/user/', self.driver.current_url)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
