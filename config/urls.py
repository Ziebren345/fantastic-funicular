from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.dashboard import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('personnel/', include('personnel.urls')),
    path('missions/', include('missions.urls')),
    path('logistics/', include('logistics.urls')),
    path('diplomacy/', include('diplomacy.urls')),
    path('intel/', include('intel.urls')),
    path('news/', include('newsfeed.urls')),
    path('', dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
