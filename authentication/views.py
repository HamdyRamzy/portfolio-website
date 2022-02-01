from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from HamdyRamzy.models import Owner, SocialMedia
from .forms import SignUp


# Create your views here.
def signup(request):
    if not request.user.is_superuser:
        return redirect('base')
    else:
        form = SignUp()
        if request.method == 'POST':
            form = SignUp(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('base')
        return render(request, 'signup.html', {'form':form})        


#Context processor for dropdow-menu view all boards in navbar
def owner_navbar_photo(request):
    photo = Owner.objects.all().first()
    context = {
        'photo':photo,
    }
    return context 


#Context processor for dropdow-menu view all boards in navbar
def owner_footer_social_links(request):
    footerLinks = SocialMedia.objects.all()
    context = {
        'footerLinks':footerLinks,
    }
    return context     