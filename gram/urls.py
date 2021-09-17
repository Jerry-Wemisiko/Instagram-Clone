from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage',views.homepage, name='homepage'),
    path('',views.signIn,name = 'signin'),
     path('signUp', views.signUp, name='signUp'),
    path('logOut', views.signOut, name='signOut'),
    path('profile', views.userprofile, name='userprofile'),
    path('add/image/', views.new_image, name='new_image'),
    path('search/', views.searchuser, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)