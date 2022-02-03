from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Owner, Contact, SocialMedia, Skill, Language, Certificate, Work, BlogPost, ProjectPost

#Render base page
def base(request):
    #Base logic
    owner = Owner.objects.all().first()
    links = SocialMedia.objects.all()
    contacts = Contact.objects.all().exclude(name='phone')
    phone = Contact.objects.get(name='phone')
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
        'phone':phone,
        'languages':languages,
        'works':works,
        'certificates':certificates,
        'blogPosts':blogPosts,
        'projectPosts':projectPosts,
    }
    return render(request, 'base.html', context)

def projects(request):
    #Projects page logic
    all_projects = ProjectPost.objects.all().order_by('-uploaded_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_projects, 3)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    context = {
        'projects_page': 'active',
        'projects': projects,
    }
    return render(request, 'projects.html', context)    
    
def blog(request):
    #Blog page logic
    all_posts = BlogPost.objects.all().order_by('-uploaded_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
    project_tags = project.tags.all()
    related_projects = ProjectPost.objects.filter(tags__in=project_tags).exclude(slug=project.slug).order_by('-uploaded_date').distinct()[:3]
    context = {
        'projects_page': 'active',
        'project': project,
        'related_projects':related_projects,
    }
    return render(request, 'project_detail.html', context)  
    

def post_detail(request, slug):
    #post detail page logic
    post = get_object_or_404(BlogPost, slug=slug)
    post_tags = post.tags.all()
    related_posts = BlogPost.objects.filter(tags__in=post_tags).exclude(slug=post.slug).order_by('-uploaded_date').distinct()[:3]
    context = {
        'blog_page': 'active',
        'post': post,
        'related_posts':related_posts,
    }
    print(post.pk)
    return render(request, 'post_detail.html', context)