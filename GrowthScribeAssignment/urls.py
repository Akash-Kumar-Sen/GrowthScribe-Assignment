from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('form/', formgiven,name='form'),
    path('data/', fetchdata,name='data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
