from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,User
# Create your views here.
def homepage(request):

    title = 'Home'
    return render(request, 'index.html',{'title':title})

@login_required(login_url= 'accounts/login')
def users(request):
    users = User.objects.all()
    page = requ
