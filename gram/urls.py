from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    path('',views.homepage, name='homepage'),
    path('su',views.signUp,name = 'signin'),
    path('signUp', views.signIn, name='signUp'),
    path('logOut', views.signOut, name='signOut'),
    path('profile', views.userprofile, name='userprofile'),
    path('search/', views.searchuser, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)