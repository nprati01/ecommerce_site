
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# connect static files and images to variables set in settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
