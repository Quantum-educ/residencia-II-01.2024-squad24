from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('user/', views.userpage, name='userpage'),
    path('user/assessment/', views.assessment, name='assessment'),
    path('user/logout/', views.user_logout, name='logout'),
]
