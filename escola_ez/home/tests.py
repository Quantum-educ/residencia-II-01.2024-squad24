from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestHomeView(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = reverse('home')
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_accessible_by_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view_anchor_signup(self):
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element('id', 'signup-anchor').click()
        self.assertIn(f'{self.live_server_url}/signup/', self.driver.current_url)

    def test_home_view_anchor_signin(self):
        self.driver.get(f'{self.live_server_url}')
        self.driver.find_element('id', 'signin-anchor').click()
        self.assertIn(f'{self.live_server_url}/signin/', self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
