from gram.models import Image, Profile,Comment
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,profileForm,uploadImageForm,commentForm,userForm
from django.shortcuts import render,redirect


# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    
    title = 'Clone'
    profile = Profile.objects.all()
    posts = Image.objects.all()
    
    return render(request, 'index.html',{'title':title,'profile':profile,'posts':posts})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'reg/regform.html',{"form": form})


@login_required(login_url='/accounts/login/')
def userprofile(request):

    if request.method == 'POST':
        userform = userForm(request.POST, instance=request.user)
        profile_form = profileForm(request.POST,request.FILES,instance=request.user)
        if profile_form.is_valid() and userform.is_valid():
            userform.save()
            profile_form.save()
            return redirect('homepage')
    else:
        profile_form = profileForm(instance=request.user)
        userform = userForm(instance=request.user)
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

@login_required(login_url='accounts/login/')
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

