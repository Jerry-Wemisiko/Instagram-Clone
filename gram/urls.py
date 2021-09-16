from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'$',views.homepage, name='homepage'),
    url(r'^signup/',views.signup_view,name ='signup'),
    url(r'^sent/', views.activation_sent_view, name="activation_sent"),
    url(r'^activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    url(r'profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)