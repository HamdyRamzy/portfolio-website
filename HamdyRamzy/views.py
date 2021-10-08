from django.shortcuts import render

# Create your views here.
#Render homepage
def home(request):
    
    return render(request, 'home.html')