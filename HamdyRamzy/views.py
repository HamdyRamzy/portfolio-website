from django.shortcuts import render, redirect, get_object_or_404
from .models import Owner, Contact, SocialMedia, Skill, Language, Certificate, Work, BlogPost, ProjectPost

#Render base page
def base(request):
    #Base logic
    owner = Owner.objects.all().first()
    links = SocialMedia.objects.all()
    contacts = Contact.objects.all()
    skills = Skill.objects.all()
    languages = Language.objects.all()
    works = Work.objects.all()
    certificates = Certificate.objects.all()
    blogPosts = BlogPost.objects.all().order_by('-uploaded_date')[:2]
    projectPosts = ProjectPost.objects.all().order_by('-uploaded_date')[:2]
    context = {
        'home_page': 'active',
        'owner':owner,
        'links':links,
        'skills':skills,
        'contacts':contacts,
        'languages':languages,
        'works':works,
        'certificates':certificates,
        'blogPosts':blogPosts,
        'projectPosts':projectPosts,
    }
    return render(request, 'base.html', context)

def projects(request):
    #Projects page logic
    projects = ProjectPost.objects.all()
    context = {
        'projects_page': 'active',
        'projects': projects,
    }
    return render(request, 'projects.html', context)    
    
def blog(request):
    #Blog page logic
    posts = BlogPost.objects.all()
    context = {
        'blog_page': 'active',
        'posts': posts,
    }
    return render(request, 'blog.html', context)    

def contact(request):
    #Contact page logic
    return render(request, 'contact.html', {'contact_page': 'active'})  

def project_detail(request, slug):
    #project detail page logic
    project = get_object_or_404(ProjectPost, slug=slug)
    context = {
        'projects_page': 'active',
        'project': project,
    }
    return render(request, 'project_detail.html', context)  
    

def post_detail(request, slug):
    #post detail page logic
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog_page': 'active',
        'post': post,
    }
    print(post.pk)
    return render(request, 'post_detail.html', context)