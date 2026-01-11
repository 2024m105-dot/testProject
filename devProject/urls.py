from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testApp.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('_debug_/',include(debug_toolbar.urls)),
    ] + urlpatterns