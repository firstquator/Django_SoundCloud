from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import music.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', music.views.home, name = "home"),
    path('music/', include('music.urls')),
    path('user/', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)