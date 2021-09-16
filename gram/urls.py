from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'$',views.homepage, name='homepage'),
    url(r'signup/',views.signup,name = 'signup'),
    url('login/', auth_views.LoginView.as_view(), name='signin'),
    url(r'profile/', views.userprofile, name='userprofile'),
    url(r'add/image/', views.new_image, name='new_image'),
    url(r'comment/<int:id>', views.comment, name='comment'),
    url('search/', views.searchuser, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)