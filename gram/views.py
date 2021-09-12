from django.shortcuts import render

# Create your views here.
def homepage(request):

    title = 'Home'
    return render(request, 'all-insta/index.html',{'title':title})
