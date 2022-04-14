from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import STATIC_URL,STATIC_ROOT
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('form/', formgiven,name='form'),
    path('data/', fetchdata,name='data'),
] + static(STATIC_URL, document_root=STATIC_ROOT)
