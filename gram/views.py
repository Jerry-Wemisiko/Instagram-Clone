from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Profile,User
from django.shortcuts import render,redirect
# Create your views here.
def homepage(request):

    title = 'Home'
    return render(request, 'index.html',{'title':title})

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')

    return render(request, 'regform.html',{'form':form})

