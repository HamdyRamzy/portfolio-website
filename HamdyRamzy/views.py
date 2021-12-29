from django.shortcuts import render

#Render base page
def base(request):
    #Base logic
    return render(request, 'base.html',{'home_page': 'active'})

def projects(request):
    #Projects page logic
    return render(request, 'projects.html', {'projects_page': 'active'})    
    
def blog(request):
    #Blog page logic
    return render(request, 'blog.html', {'blog_page': 'active'})    

def contact(request):
    #Contact page logic
    return render(request, 'contact.html', {'contact_page': 'active'})  

def project_detail(request):
    #Contact page logic
    return render(request, 'project_detail.html')  
    

def post_detail(request):
    #Contact page logic
    return render(request, 'post_detail.html')  