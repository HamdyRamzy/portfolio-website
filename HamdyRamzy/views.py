from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from HamdyRamzy.forms import ContactMeForm
from .models import Owner, Contact, SocialMedia, Skill, Language, Certificate, Work, BlogPost, ProjectPost, Visitor, SiteInfo, Project_image
from django.utils import timezone
from .utils import get_ip_address
from itertools import chain

#Render base page
def base(request):
    #Base logic
    owner = Owner.objects.all().first()
    links = SocialMedia.objects.all()
    contacts = Contact.objects.all().exclude(name='phone')
    phone = Contact.objects.get(name='phone')
    skills = Skill.objects.all()[:4]
    all_skills = Skill.objects.all()
    skills_count = Skill.objects.all().count()
    languages = Language.objects.all()
    works = Work.objects.all()[:3]
    all_works = Work.objects.all()
    works_count = Work.objects.all().count()
    certificates = Certificate.objects.all()[:3]
    all_certificates = Certificate.objects.all()
    certificates_count = Certificate.objects.all().count()
    blogPosts = BlogPost.objects.all().order_by('-uploaded_date')[:2]
    blogPosts_count = BlogPost.objects.all().count()
    projectPosts = ProjectPost.objects.all().order_by('-uploaded_date')[:2]
    projectPosts_count = ProjectPost.objects.all().count()
    site = SiteInfo.objects.all().first()
    context = {
        'home_page': 'active',
        'owner':owner,
        'links':links,
        'skills':skills,
        'all_works':all_works,
        'all_skills':all_skills,
        'skills_count':skills_count,
        'contacts':contacts,
        'phone':phone,
        'languages':languages,
        'works':works,
        'works_count':works_count,
        'certificates':certificates,
        'all_certificates':all_certificates,
        'certificates_count':certificates_count,
        'blogPosts':blogPosts,
        'projectPosts':projectPosts,
        'blogPosts_count':blogPosts_count,
        'projectPosts_count':projectPosts_count,
        'site':site,
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
    links = SocialMedia.objects.all().exclude(name='github')
    phone = Contact.objects.get(name='phone')
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        sender = get_ip_address(request)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.save()
            return redirect('sent')
        else:
            context = {'form': form,
            'contact_page': 'active',
            'links':links,
            'phone':phone,
            }
            return render(request, 'contact.html', context)     
    form = ContactMeForm()
    context = {'form': form,
    'contact_page': 'active',
    'links':links,
    'phone':phone,
    }
    return render(request, 'contact.html', context)  

def project_detail(request, slug):
    #project detail page logic
    project = get_object_or_404(ProjectPost, slug=slug)
    project_tags = project.tags.all()
    related_projects = ProjectPost.objects.filter(tags__in=project_tags).exclude(slug=project.slug).order_by('-uploaded_date').distinct()[:3]
    project_images = Project_image.objects.filter(project__slug=slug)
    session_key = 'view_poject_{}'.format(project.slug)
    if not request.session.get(session_key,False):
        project.views +=1
        project.save()
        request.session[session_key] = True
    context = {
        'projects_page': 'active',
        'project': project,
        'related_projects':related_projects,
        'project_images':project_images,
    }
    return render(request, 'project_detail.html', context)  
    

def post_detail(request, slug):
    #post detail page logic
    post = get_object_or_404(BlogPost, slug=slug)
    post_tags = post.tags.all()
    related_posts = BlogPost.objects.filter(tags__in=post_tags).exclude(slug=post.slug).order_by('-uploaded_date').distinct()[:3]
    session_key = 'view_post_{}'.format(post.slug)
    if not request.session.get(session_key,False):
        post.views +=1
        post.save()
        request.session[session_key] = True
    context = {
        'blog_page': 'active',
        'post': post,
        'related_posts':related_posts,
    }
    return render(request, 'post_detail.html', context)

#Handle search about bolg posts and projects.
def search(request):
    if request.method == 'GET':
        search_str = request.GET['searchField']

        posts = BlogPost.objects.filter(title__icontains = search_str).order_by('-uploaded_date')|BlogPost.objects.filter(description__icontains = search_str).order_by('-uploaded_date')
        projects = ProjectPost.objects.filter(title__icontains = search_str).order_by('-uploaded_date')|ProjectPost.objects.filter(description__icontains = search_str).order_by('-uploaded_date')
        posts_count = posts.count()   
        projects_count = projects.count() 
        all_results = list(chain(posts, projects))
        results_count = (posts_count + projects_count)
        
        context = {'posts':posts,
                'projects':projects,
                'posts_count':posts_count,
                'projects_count':projects_count,
                'search_str':search_str,
                'results_count':results_count,
                'all_results':all_results,
                }
        return render(request, 'search.html', context)    


def sent(request):        
    return render(request, 'sent.html')        


def sent(request):        
    return render(request, 'sent.html')        



def visitors(request):
    visitors_count = Visitor.objects.all().count()
    ip = get_ip_address(request)
    user = Visitor(viewer=ip)
    visitor = Visitor.objects.filter(viewer=ip).first()
    if not visitor:
        user.last_visit =timezone.now()
        user.save()
    else:
        visitor.last_visit = timezone.now()
        visitor.save()
    context = {'visitors_count': visitors_count,
            }    
    return context  
