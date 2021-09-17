from gram.models import Image, Profile,Comment,Users
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from gram.forms import SignUpForm,profileForm,uploadImageForm,commentForm
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
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = username = request.POST['fullname']
            email = request.POST['email']
            print(email)
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
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in succesfully")
            return redirect('homepage')

    return render(request, 'reg/login.html')

def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Successfully logged Out!")
    return redirect("signIn") 

def userprofile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        photo= request.FILES['photo']
        bio = request.POST['bio']

    return render(request, 'profile.html', {"userform": userform, "profile_form": profile_form})


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

def comment(request, image_id):
    current_user = request.user
    images = Image.objects.get(id=image_id)
    userprofile = Profile.objects.get(username=current_user)
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image_post = images
            comment.comment_by = userprofile
            comment.save()
        return redirect('homepage')
    else:
        form = commentForm()
    return render(request, 'new_comment.html', {"form": form, "images": images, 'comments': comments})

