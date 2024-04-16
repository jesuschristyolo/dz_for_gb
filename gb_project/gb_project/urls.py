from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_app/', include('hello_app.urls', namespace="hello_app")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
