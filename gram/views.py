from gram.models import Image, Profile,Users
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def homepage(request):
    
    title = 'Clone'
    profile = Profile.objects.all()
    posts = Image.objects.all()
    
    return render(request, 'index.html',{'title':title,'profile':profile,'posts':posts})

def signUp(request):
    if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                user = Users(username=username, email=email,password=make_password(password))
                user.save()
                messages.add_message(request, messages.SUCCESS, "Account created successfully!")
                return redirect('signIn')
            else:
                print("Passsword is incorrect")
    return render(request, 'reg/regform.html')
  
def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in succesfully")
            return redirect('homepage')
        else:
            print('User not found')
    return render(request, 'reg/login.html')

def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Successfully logged Out!")
    return redirect("signIn") 

def userprofile(request):
    profiles = Profile.objects.all()
    posts = Image.objects.all()

    return render(request, 'profile.html',)


def searchuser(request):
    if 'gram' in request.GET and request.GET['gram']:
        name = request.GET.get("gram")
        search_results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': search_results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for a user"
    return render(request, 'search.html', {'message': message})


def new_image(request):
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = uploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.profile = request.user.profile
            new_post.save()
            return redirect('homepage')
    else:
        form = uploadImageForm()
    return render(request, 'new_image.html', {"form": form})

