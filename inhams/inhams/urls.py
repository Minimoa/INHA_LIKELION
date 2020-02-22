from django.contrib import admin
from django.urls import path, include
import ms.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ms.views.home,name="home"),
    path('word/',include('ms.urls')),
    path('sort_alphabet', ms.views.sort_alphabet, name='sort_alphabet'),
    path('sort_date', ms.views.sort_date, name='sort_date'),
]
