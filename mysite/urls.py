from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),
    path('', include('django_prometheus.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
