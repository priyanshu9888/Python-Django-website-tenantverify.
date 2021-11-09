"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


admin.site.site_header = "Tenantverify Admin"
admin.site.site_title = "Tenantverify Admin Portal"
admin.site.index_title = "Welcome to Tenantverify"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('apointment/', include('home.urls')),
    path('index/', include('home.urls')),
    path('home/', include('home.urls')),
    path('about/', include('home.urls')),
    path('cancel/', include('home.urls')),
    path('contact/', include('home.urls')),
    path('media/', include('home.urls')),
    path('service/', include('home.urls')),
    path('login/', include('home.urls')),
    path('signup/', include('home.urls')),
    path('forgot/', include('home.urls')),
    path('form/' , include('home.urls')),





    
   
]
from django.conf import settings
from django.conf.urls.static import static

