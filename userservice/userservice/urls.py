from django.conf.urls import url, include
from django.contrib import admin

from userservice import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
 
    url(r'^$', views.api_root),
    url(r'^', include('user.urls', namespace='user')),
]