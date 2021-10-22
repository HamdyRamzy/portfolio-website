from django.shortcuts import render


#Render base page
def base(request):
    #Base logic
    return render(request, 'base.html')

def projects(request):
    #Projects page logic
    return render(request, 'projects.html')    

    
def blog(request):
    #Blog page logic
    return render(request, 'blog.html')    


def contact(request):
    #Contact page logic
    return render(request, 'contact.html')  