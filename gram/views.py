from django.shortcuts import render
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
from .models import Image,Profile,User
from django.shortcuts import render,redirect


# Create your views here.
def homepage(request):

    title = 'Home'
    return render(request, 'index.html',{'title':title})

def SignUp(request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
        else:
            form = SignUpForm()
        return render(request, 'regform.html',{'form':form})

