from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users import views
from users.apps import UsersConfig
from users.views import UserLoginView, UserRegisterView, UserProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', UserRegisterView.as_view(template_name='users/register.html'), name='register'),
    path('verify_message/', TemplateView.as_view(template_name='users/verify_message.html'), name='verify_message'),
    path('success_message/', TemplateView.as_view(template_name='users/success_message.html'), name='success_message'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]