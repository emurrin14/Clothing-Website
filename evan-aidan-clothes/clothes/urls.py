# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include
# Import the necessary helpers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Make sure you have a path to your clothesshop app's urls
    path('shop/', include('clothesshop.urls')),
]

# Add this line to serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)