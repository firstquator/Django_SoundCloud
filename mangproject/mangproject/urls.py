from django.contrib import admin
from django.urls import include, path
from . import music

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', music.views.home, name = "home"),
    path('music/', include('music.urls')),
    path('user/', include('user.urls')),
]
