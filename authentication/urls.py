from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as  auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True ,template_name='login.html'), name='login'),
]