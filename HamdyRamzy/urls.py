from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name="base"),
	path('projects/', views.projects, name="projects"),
	path('blog/', views.blog, name="blog"),
	path('contact/', views.contact, name="contact"),

]