from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage',views.homepage, name='homepage'),
    path('',views.signup,name = 'signup'),
    path('login', auth_views.LoginView.as_view(), name='signin'),
    path('profile', views.userprofile, name='userprofile'),
    path('add/image/', views.new_image, name='new_image'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('search/', views.searchuser, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)