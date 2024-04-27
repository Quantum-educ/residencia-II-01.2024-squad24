from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('user/', views.userpage, name='userpage'),
    path('user/assessments/ned/', views.ned_assessment, name='ned_assessment'),
    path('user/assessments/vak/', views.vak_assessment, name='vak_assessment'),
    path('user/assessments/history/', views.assessments_history, name='assessments_history'),
    path('user/assessments/result/', views.assessment_result, name='assessment_result'),
    path('user/logout/', views.user_logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
