from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='')),
    path('api/', include('api.urls')),
    path('', include('main.urls', namespace='')),
    path('captcha', include('captcha.urls')),
    path('', include('main.urls', namespace='')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)