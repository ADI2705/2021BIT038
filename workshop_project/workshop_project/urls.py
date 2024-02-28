from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workshop/', include('workshop_app.urls')),
    # Add other app URLs or custom URLs as needed
]
