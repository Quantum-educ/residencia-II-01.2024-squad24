from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from users.forms import StudentSignUpForm


class TestSignUpView(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('signup')
        cls.data = {
            'username': 'user',
            'email': 'user@email.com',
            'password': 'password',
            'confirm_password': 'password',
            'accept_terms': True,
        }
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_signup_url_exists_at_desired_location(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_accessible_by_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_view_template(self):
        self.driver.get(f'{self.live_server_url}/signup/')
        self.driver.find_element('id', 'id_username').send_keys(self.data.get('username'))
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self.driver.find_element('id', 'id_confirm_password').send_keys(self.data.get('confirm_password'))
        self.driver.find_element('id', 'id_accept_terms').click()
        self.driver.find_element('id', 'submit').click()
        self.assertIn(f'{self.live_server_url}/user/', self.driver.current_url)

    def _submit_and_assert_still(self):
        self.driver.find_element('id', 'submit').click()
        self.assertIn(f'{self.live_server_url}/signup/', self.driver.current_url)
    
    def test_signup_view_required_fields(self):
        self.driver.get(f'{self.live_server_url}/signup/')
        self._submit_and_assert_still()
        self.driver.find_element('id', 'id_username').send_keys(self.data.get('username'))
        self._submit_and_assert_still()
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self._submit_and_assert_still()
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self._submit_and_assert_still()
        self.driver.find_element('id', 'id_confirm_password').send_keys(self.data.get('confirm_password'))
        self._submit_and_assert_still()
    
    def test_signup_view_short_passwords(self):
        self.driver.get(f'{self.live_server_url}/signup/')
        self.driver.find_element('id', 'id_username').send_keys(self.data.get('username'))
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys('shortPw')
        self.driver.find_element('id', 'id_confirm_password').send_keys('shortPw')
        self.driver.find_element('id', 'id_accept_terms').click()
        self._submit_and_assert_still()
    
    def test_signup_view_mismatched_passwords(self):
        self.driver.get(f'{self.live_server_url}/signup/')
        self.driver.find_element('id', 'id_username').send_keys(self.data.get('username'))
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self.driver.find_element('id', 'id_confirm_password').send_keys('mismatched')
        self.driver.find_element('id', 'id_accept_terms').click()
        self._submit_and_assert_still()
    
    def test_signup_view_email_already_registered(self):
        form = StudentSignUpForm(data=self.data)
        form.save()
        self.driver.get(f'{self.live_server_url}/signup/')
        self.driver.find_element('id', 'id_username').send_keys(self.data.get('username'))
        self.driver.find_element('id', 'id_email').send_keys(self.data.get('email'))
        self.driver.find_element('id', 'id_password').send_keys(self.data.get('password'))
        self.driver.find_element('id', 'id_confirm_password').send_keys(self.data.get('confirm_password'))
        self.driver.find_element('id', 'id_accept_terms').click()
        self._submit_and_assert_still()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
