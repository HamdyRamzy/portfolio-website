from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
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