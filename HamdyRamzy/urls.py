from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.base, name="base"),
	path('search/', views.search, name='search'),
	path('sent/', views.sent, name='sent'),
	path('projects/', views.projects, name="projects"),
	path('projects/<slug:slug>/', views.project_detail, name="project-detail"),
	path('blog/<slug:slug>/', views.post_detail, name="post-detail"),
	path('blog/', views.blog, name="blog"),
	path('contact/', views.contact, name="contact"),
	path('visitors/', views.visitors, name="visitors"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)