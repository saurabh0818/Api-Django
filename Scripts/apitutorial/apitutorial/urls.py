
from django.contrib import admin
from django.urls import path, include
import webapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include('webapi.urls'))
]
