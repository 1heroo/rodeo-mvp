"""rodeo_kg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from rodeo_kg import settings


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1/user-auth/', include('users.urls')),
    path('api/v1/', include('tournaments.urls')),
    path('api/v1/', include('news.urls')),
    path('api/v1/', include('paybox.urls'))

] + swagger + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
