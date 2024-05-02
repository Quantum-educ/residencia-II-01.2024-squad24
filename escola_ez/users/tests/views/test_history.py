from django.test import TestCase
from django.urls import reverse
from users.models import Student, Profile
from users.assessments.ned_model import NedAssessment  
from users.assessments.vak_model import VAKAssessment 
from django.shortcuts import render

class AssessmentsHistoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self): 
        profile = Profile.objects.create()
        self.user = Student.objects.create(username='user', email='user@email.com', profile=profile)
        self.user.set_password('12345')
        self.user.save()  
    
    def test_view_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('assessments_history'))
        self.assertEqual(response.status_code, 302)  

    def test_view_accessible_by_name(self):
        self.client.login(username='user', password='12345')  
        response = self.client.get(reverse('assessments_history'), follow=True)
        self.assertEqual(response.status_code, 200)    
        
    def assessments_history(request):
        ned_assessments = NedAssessment.objects.all()
        vak_assessments = VAKAssessment.objects.all()
        return render(request, 'assessments_history.html', {'ned_assessments': ned_assessments, 'vak_assessments': vak_assessments})
    
    