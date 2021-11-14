from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name="base"),
	path('projects/', views.projects, name="projects"),
	path('projects/How-can-link-flutter-with-django', views.project_detail, name="project-detail"),
	path('blog/', views.blog, name="blog"),
	path('contact/', views.contact, name="contact"),

]